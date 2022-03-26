import random
import hangman_art
import hangman_words

#dictionary
chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#art header.
print(hangman_art.logo)
#Testing code
#print(f"The solution is {chosen_word}.")

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #Check dup
    if guess in display:
        print(f"You already said {guess}")
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #Test code
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        print(f"{guess} is not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    
    print(f"{' '.join(display)}")

    #Check win
    if "_" not in display:
        end_of_game = True
        print("You win.")

    
    print(hangman_art.stages[lives])