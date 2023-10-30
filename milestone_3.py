import random
word_list = ['lemon', 'grape', 'banana', 'strawberry', 'kiwi']
word = random.choice(word_list)

print(word)

def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print(f'Good guess! {guess} is in the word')
    elif guess not in word:
        print(f'Sorry {guess} is not in the word, try again')
    else: 
        print('Something went wrong with finding letter in word')

def ask_for_input():
    while True:
        guess = input('Input a single letter ')
        if guess.isalpha() == True and len(guess) == 1:
            break
        elif guess.isalpha() == False: 
            print('Invalid letter. Please enter a single alphabetical character')
        elif len(guess) != 1:
            print('Please only enter one character')
        else:
            print('Something went wrong with the letter entry')

    check_guess(guess)

ask_for_input()