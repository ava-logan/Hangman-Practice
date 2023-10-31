import random
word_list = ['lemon', 'grape', 'banana', 'strawberry', 'kiwi']
word = random.choice(word_list)

class Hangman:
    def __init__(self, random_word, num_lives=5):
        self.random_word = list(random_word)
        self.word_guessed = list('-'*len(random_word))
        self.num_letters = len(random_word)
        self.num_lives = 5
        self.list_of_guesses = []

    def find_indexes(self, guess):
        print('made it to the find index method')
        guess_letter_index_list = []
        while guess in self.random_word:
            guess_index = self.random_word.index(guess)
            guess_letter_index_list.append(guess_index)
            self.random_word[guess_index] = '-'
            print('The indices of the guess is ', guess_letter_index_list)    #rm later - shows index of guessed word
            print('The random word that you DONT KNOW has these letters left', self.random_word) #rm later - shows that all occurences of the guess have been acknowledged
        return guess_letter_index_list

    def update_hidden_word(self, guess):
        for numbers in Hangman.find_indexes(self, guess):
            self.word_guessed[numbers] = guess
            print('So far the word youve guessed is',self.word_guessed) #format later - shows guess so far 

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.random_word:
            print(f'Good guess! {guess} is in the word')
            Hangman.find_indexes(self, guess)
            Hangman.update_hidden_word(self, guess)
        elif guess not in self.random_word:
            print(f'Sorry {guess} is not in the word')
        else: 
            print('Something went wrong with finding letter in word')

    def win_lose_or_continue(self):
        while True: 
            if self.num_lives == 0:
                print(f'Game over! You have 0 lives left! The word was {self.random_word}')
                break
            elif self.num_lives > 0 and self.num_letters == 0:
                print(f'You have won the game! Congratulations')
                break 
            elif self.num_lives > 0 and self.num_letters > 0:
                print(f'You have {self.num_lives} remaining')
                print(f'You have so far guessed {self.list_of_guesses}')
            else:
                print('Something went wrong with the win/lose/continue method')

    def ask_for_input(self):
        while True: 
            guess = input("Please enter a letter ")
            if guess.isalpha() == False or len(guess) != 1:
                print('Invalid entry, must be a single, alphabetical character')
            elif guess in self.list_of_guesses:
                print("You have already tried that letter")
            elif len(guess) == 1 and guess.isalpha() == True:
                Hangman.check_guess(self, guess)
                self.num_lives -=1     
                self.list_of_guesses.append(guess)
                self.num_letters -= len(Hangman.find_indexes(self, guess))
            else: 
                print('Something went wrong with the input')
    
    def what_went_wrong(self):
        print(self.random_word)
        print(type(self.random_word))
        print(self.word_guessed)
        print(self.num_letters)
        print(self.num_lives)
        print(self.list_of_guesses) 

def play_game(word_list):
    word = random.choice(word_list)
    game = Hangman(word)
    game.ask_for_input()
    
#play_game(word_list)