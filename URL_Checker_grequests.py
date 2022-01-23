import grequests

with open("urls.txt", "r") as input_file:
    urls = [url.strip() for url in input_file.readlines()]


def exception(self, request, exception_details):
    print("Problem: {}: {}".format(request.url, exception_details))


with open("foundurls.txt", 'w') as output_file:
    responses = grequests.map((grequests.get(u) for u in urls), exception_handler=exception, size=100)
    for result in zip(urls, responses):
        output_file.write(f"{result}\n")
