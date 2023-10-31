import random
word_list = ['lemon', 'grape', 'banana', 'strawberry', 'kiwi']
another_word_list = ['caterpillar', 'rabbit', 'turtle', 'crocodile', 'elephant']

class Hangman:
    def __init__(self, random_word, num_lives=5):
        self.random_word = list(random_word)
        self.word_guessed = list('-'*len(random_word))
        self.num_letters = len(random_word)
        self.num_lives = 5
        self.list_of_guesses = []

    def find_indexes(self, guess):
        guess_letter_index_list = []
        while guess in self.random_word:
            guess_index = self.random_word.index(guess)
            guess_letter_index_list.append(guess_index)
            self.random_word[guess_index] = '-'
        return guess_letter_index_list

    def update_hidden_word(self, guess):
        for numbers in Hangman.find_indexes(self, guess):
            self.word_guessed[numbers] = guess

    def update_num_letters(self, guess):
        numbers = len(Hangman.find_indexes(self, guess))
        self.num_letters = self.num_letters - numbers

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.random_word:
            print(f'Good guess! {guess} is in the word')
            Hangman.find_indexes(self, guess)
            Hangman.update_hidden_word(self, guess)
            Hangman.update_num_letters(self, guess)
        elif guess not in self.random_word:
            print(f'Sorry {guess} is not in the word')
            self.num_lives = self.num_lives -1 
        else: 
            print('Something went wrong with finding letter in word')

    def ask_for_input(self):
            guess = input("Please enter a letter ")
            if guess.isalpha() == False or len(guess) != 1:
                print('Invalid entry, must be a single, alphabetical character')
            elif guess in self.list_of_guesses:
                print("You have already tried that letter")
            elif len(guess) == 1 and guess.isalpha() == True:
                Hangman.check_guess(self, guess)       
                self.list_of_guesses.append(guess)
                return self.num_lives, self.num_letters
            else: 
                print('Something went wrong with the input')
    
    def what_went_wrong(self):
        print(self.random_word)
        print(type(self.random_word))
        print(self.word_guessed)
        print(self.num_letters)
        print(self.num_lives)
        print(self.list_of_guesses) 

        
def play_game(another_word_list):
    word_selector = random.choice(another_word_list)
    game = Hangman(word_selector)    
    while True:
        Hangman.ask_for_input()
        if num_lives == 0:
            print(f'Game over! You have 0 lives left! The word was {self.random_word}')
            break
        elif num_lives > 0 and num_letters == 0:
            print(f'You have won the game! Congratulations')
            break
        elif num_lives > 0 and num_letters > 0:
            print(f'Lives: {self.num_lives}, Word guessed fo far: {self.word_guessed}. Letters guessed: {self.list_of_guesses}')
        else:
            print('Something went wrong with the win/lose/continue method')
        

play_game(another_word_list)