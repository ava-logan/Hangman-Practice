import random
word_list = ['lemon', 'grape', 'banana', 'strawberry', 'kiwi']
word = random.choice(word_list)

class Hangman:
    def __init__(self, random_word, num_lives=5):
        self.random_word = random_word
        self.word_guessed = list('-'*len(word))
        self.num_letters = len(word)
        self.num_lives = 5
        self.list_of_guesses = []

    def check_guess(self, guess):
        if guess in self.random_word:
            print(f'Good guess! {guess} is in the word')
        elif guess not in self.random_word:
            print(f'Sorry {guess} is not in the word')
        else: 
            print('Something went wrong with finding letter in word')

    def ask_for_input(self):
        while True: 
            guess = input("Please enter a letter ")
            guess = guess.lower()
            if guess.isalpha() == False or len(guess) != 1:
                print('Invalid entry, must be a single, alphabetical character')
            elif guess in self.list_of_guesses:
                print("You have already tried that letter")
            elif guess.isalpha == True and len(guess) == 1:
                Hangman.check_guess(guess)
                self.list_of_guesses.append(guess)
            else: 
                print('Something went wrong with the input')
    
    def what_went_wrong(self):
        print(self.random_word)
        print(self.word_guessed)
        print(self.num_letters)
        print(self.num_lives)
        print(self.list_of_guesses) 
