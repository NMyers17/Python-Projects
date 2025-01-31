import random
from hangman_words import word_list
from hangman_art import stages
from hangman_art import logo

lives = 6

print(logo)
chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        elif guess == display:
            print(guess)
            print("You've already guessed that.")
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word:
        lives -= 1
        print(guess)
        print("This letter is not in the word. You lose a life.")

        if lives == 0:
            game_over = True
            print("***********************YOU LOSE**********************")
            print(f"The letter you were trying to guess was {chosen_word}")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    print(stages[lives])