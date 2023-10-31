# Hangman-Practice

## Table of contents 
1. Overview
2. Methods
   
   a. Init
   
   b. Find Indexes
   
   c. Update Word guessed
   
   d. Update Number of Letters
   
   e. Check Guess
   
   f. Ask For Input
   
3. Flow chart 

## 1. Overview 
This is a program designed to play hangman. Firstly, a word is randomly chosen from a list. Them, the player is asked to input a letter which is passed through a class. Here, it is determined whether the letter is part of a random word. Approprite methods are run, which will be explained below, and the game continues until it is won. 

## 2. Methods

### a. Init 
self.random_word : list. The word that is being guessed. Selected from a defined list in the play_game function outside the class. Converted from a string to a list for the ease of accessing characters according to their index. 
self.word_guessed: list. A string of placeholders ‘-’ representing each character of the random_word. Variable is also in string format for ease of changing the characters. 
self.num_letters: integer. The length of the random_word being guessed.  
self.num_lives: integer. The number of attempts the user has to guess the word. 
self.list_of_guesses: list. The list of valid characters the user has already guessed. 
self.guess_letter_index_list: list. A list of indices of the current guess in the random_word. Reverts to an empty list before a new correct guess is passed through the Class. 


### b. Find_indexes
Outcome: Finds all occurrences of the guess character in the random_word and creates a list of their indices. 

Purpose: The indices list is required in the update_word_guessed and update_num_letters methods later. 

Execution:  
Checks that the guess is in the random_word 
1. If true: A variable ‘guess_index’ is created. Pythons built in function index() is used to find the first instance of the guess. The index is assigned to guess_index 
2. The list self.random_letter_index_list is updated with this instance of the index using append() 
3. The index is used to reassign the instance of the guess to a blank ‘-’ character 

If there is another instance of the guess in the random_word 1-4 is repeated. As the previous instances have been replaced with ‘-’ the next occurrence will be retrieved. Thus, ensuring if a word has the same letter more than once all occurrences are noted.  

1. If false: doesn’t run. This occurs when all occurrences of the guess character have been retrieved. 


### c. Update Word Guessed
Outcome: changes the word_guessed variable to replace ‘-’ with all occurrences of the guessed character in their correct location 

Purpose: the user can keep track of how much of the word they have guessed correctly, and use the revealed characters to influence their next guess 

Execution: 
1. Iterates through the self.guess_letter_index_list (created from find_indexes method) 
2. For each index in the list, its corresponding index in word_guessed is replaced with the guessed character 

 
##d. Update Number of Letters 
Outcome: the self.num_letters variable is changed so that it is equal to the number of ‘-’ left in word_guessed.  

Purpose: if the number of letters left is 0 then the user has completely guessed the random_word and this declares that the user has won.  

Execution:  
1. The length of the self.guess_letter_index_list (from find_indexes method) is found using the len() function and assigned to a local variable named numbers 
2. The self.num_letters is deducted by the numbers variable 


### D. Check Guess
Purpose: takes the valid input from the user and selects 1 of 2 pathways depending on whether that character is, or is not, present in the random_word 

Execution and outcomes:  

Pathway 1: The character is present in the word 
1. Prints that the guess is present  
2. Redefines the guess_letter_index_list back to an empty list, erasing any data from previous instances  
3. Initiates the find_indexes method 
4. Initiates update_word_guessed method 
5. Initiates update_num_letters method 

Outcome:  
- Random_word has all occurences of the guess redacted
- Word_guessed has all occurrences of the guess introduced in their corresponding indices
- Num_letters is reduced to fit the number of blank characters left to guess 

Pathway 2: The character isnt present in the word 
1. Prints that the guess is not present  
2. Reduces the number of lives by 1 

Outcome: the player loses a life for their incorrect guess 


### E. Ask For Input
Purpose: asks the user to input a guess. Before passing the guess to other methods, ensures that the entry is a singular, alphabetical character. This ensures invalid inputs aren't used and an efficient run of the program.  

Execution: 
In a while True loop the user is asked to enter a letter, which is assigned to the variable guess 

Pathway 1: the entry is not alphabetical or a single character 
1. Prints ‘invalid entry, must be a single, alphabetical character’
2. Loop is commenced again, and user is asked for another entry

Pathway 2: the entry has already been tried
1. Prints ‘you have already tried that letter’
2. Loop is commenced again, and user is asked for another entry 

Pathway 3: a single, alphabetical character is entered 
1. Check_guess method is run
2. The list of guesses is updated to include the new entry
3. The user is shown the number of lives remaining, a list of the letters guessed and the appearance of the word so far.
4. The while loop is broken  

Outcome: All the same as check guess: 
- Random_word has all occurences of the guess redacted
- Word_guessed has all occurrences of the guess introduced in their corresponding indices
- Num_letters is reduced to fit the number of blank characters left to guess 

Plus:  
- The list of previous guesses has been updated
- All the relevant changes are complied into a message for the user  

## 3. Flow diagram 
<img width="1440" alt="Screenshot 2023-10-31 at 22 28 33" src="https://github.com/ava-logan/Hangman-Practice/assets/148722602/5c08eed2-d595-41dd-bd07-2a019f69f41e">

## 4. Other things for a readme.file 
- installation instructions
- usage instructions
- file structure
- liscence information


