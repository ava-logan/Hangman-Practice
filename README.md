# Hangman-Practice

## Methods

### __init__ 

### find_indexes
Purpose: To find all occurences of the letter guessed (guess) by the user.

As the index() function only returns the first instance of the argument passed, every time the letter is retrieved it is replaced with a '-'. A 
While loop then continues to seach for the guess in the random_word until there are no occurences. A list is created called guess_letter_index_list 
whihc is returned to update the word_guessed variable. While the replace() function could have be used for the find_indexes method, the index list is 
essential to mutate the word_guessed variable at the correct locations. 

### update_hidden_word
Purpose: to mutate the hidden_word to reveal the letters in their correct location.

Having a visual for where the letters are reflects how the game is traditionally played and adds to the fun of the game. 

### check_guess
Purpose: searches for the guess in the random_word

If found: will call the find_index and update_hidden_word method to update the current status of the empty guess (word_guessed) and remove it from the hidden status of the current word

If not found: will print 'guess not found' and return to ask_for_input. No changes are made to the hidden_word or the random_word

### ask_for_input

### what_went_wrong 


## How to play
