import random
word_list = ['lemon', 'grape', 'banana', 'strawberry', 'kiwi']
word = random.choice(word_list)

class Hangman:
    def __init__(self, words_list, num_lives=5):
        self.word = word
        self.word_guessed = list('-'*len(word))
        self.num_letters = len(word)
        self.num_lives = 5
        self.word_list = word_list
        self.list_of_guesses = []

    def check_guess(guess):
        if guess in word:
            print(f'Good guess! {guess} is in the word')
        elif guess not in word:
            print(f'Sorry {guess} is not in the word')
        else: 
            print('Something went wrong with finding letter in word')

    def ask_for_input():
        while True: 
            guess = input("Please enter a letter ")
            guess = guess.lower()
            if guess.isalpha() == False or len(guess) != 1:
                print('Invalid entry, must be a single, alphabetical character')
            elif guess in list_of_guesses:
                print("You have already tried that letter")
            elif guess.isalpha == True and len(guess) == 1:
                Hangman.check_guess(guess)
                list_of_guesses.append(guess)
            else: 
                print('Something went wrong with the input')

Hangman.ask_for_input()