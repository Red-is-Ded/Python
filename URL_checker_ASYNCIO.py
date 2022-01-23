

#!/usr/bin/env python3
# asynctest.py

import asyncio

import logging
import sys
from typing import IO

import aiofiles
import aiohttp
from aiohttp import ClientSession, TCPConnector
from aiolimiter import AsyncLimiter


# Configure limiter to see if this makes any different to the request blocking.
# Tried as low as 10 requests in 10 seconds and it doesn't seem to make any difference
limiter = AsyncLimiter(100,10)

logging.basicConfig(
    format="%(asctime)s %(levelname)s:%(name)s: %(message)s",
    level=logging.DEBUG,
    datefmt="%H:%M:%S",
    stream=sys.stderr,
)
logger = logging.getLogger("areq")
logging.getLogger("chardet.charsetprober").disabled = True


async def fetch_status(url: str, session: ClientSession, **kwargs) -> str:
    # Make the request and return the response status
    # Note - this DOES NOT just do a header-get, unlike serial version of code
    resp = await session.request(method="GET", url=url, **kwargs)
    logger.info("Got response [%s] for URL: %s", resp.status, url)
    return resp.status


async def parse(url: str, session: ClientSession, **kwargs) -> set:
    async with limiter:
        # Return status of the respective URL request
        found = set()
        try:
            status = await fetch_status(url=url, session=session, **kwargs)
        except (
            aiohttp.ClientError,
            aiohttp.http_exceptions.HttpProcessingError,
        ) as e:
            logger.error(
                "aiohttp exception for %s [%s]: %s",
                url,
                getattr(e, "status", '61'),
                getattr(e, "message", '62'),
            )
            return found
        except asyncio.TimeoutError:
            logger.exception(
                "Timeout occured:  %s", url
            )
            found.add('timeout')
            return found
        except Exception as e:
            logger.exception(
                "Non-aiohttp exception occured:  %s", getattr(e, "__dict__", {})
            )
            found.add(status)
            return found
        else:
            found.add(status)

            return found

async def write_one(file: IO, url: str, **kwargs) -> None:
    # Write the returned statuses and URLs to file
    res = await parse(url=url, **kwargs)
    if not res:
        return None
    async with aiofiles.open(file, "a") as f:
        for p in res:
            await f.write(f"{url}\t{p}\n")
        logger.info("Wrote results for source URL: %s", url)

async def bulk_crawl_and_write(file: IO, urls: set, **kwargs) -> None:
    # Iterate over URLs provided and spin up individual tasks
    # Note - TCPconnector forcing SSL=False to prevent SSL handling errors when making the request
    async with ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
        tasks = []
        for url in urls:
            tasks.append(
                write_one(file=file, url=url, session=session, **kwargs)
            )
        await asyncio.gather(*tasks)



if __name__ == "__main__":
    import pathlib
    import sys

    assert sys.version_info >= (3, 7), "Script requires Python 3.7+."
    here = pathlib.Path(__file__).parent

    with open(here.joinpath("urls.txt")) as infile:
        urls = set(map(str.strip, infile))

    outpath = here.joinpath("foundurls.txt")
    with open(outpath, "w") as outfile:
        outfile.write("source_url\tstatus\n")

    asyncio.run(bulk_crawl_and_write(file=outpath, urls=urls))