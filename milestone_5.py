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
        while True:
            guess = input("Please enter a letter ")
            if guess.isalpha() == False or len(guess) != 1:
                print('Invalid entry, must be a single, alphabetical character')
            elif guess in self.list_of_guesses:
                print("You have already tried that letter")
            elif len(guess) == 1 and guess.isalpha() == True:
                Hangman.check_guess(self, guess)       
                self.list_of_guesses.append(guess)
                print(f'Lives: {self.num_lives}. Letters guessed: {"".join(self.list_of_guesses)}. Word so far: {self.word_guessed}')
                break
            else: 
                print('Something went wrong with the input')
    
    def what_went_wrong(self):
        print(self.random_word)
        print(type(self.random_word))
        print(self.word_guessed)
        print(self.num_letters)
        print(self.num_lives)
        print(self.list_of_guesses) 

def play_game(another_word_list, game_num_lives):
    word_selector = random.choice(another_word_list)
    game = Hangman(word_selector)
    while game.num_lives > -1 or game.num_letters > -1:
        if game.num_lives == 0:
            print('Game Over')
            break
        elif game.num_letters == 0 and game.num_lives != 0:
            print("You win")
            break
        elif game.num_letters > 0 and game.num_lives > 0:
            game.ask_for_input()
        else: 
            print('Something went wrong with the play_game loop')
            break



play_game(another_word_list, 3)