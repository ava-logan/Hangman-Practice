import random
word_list = ['lemon', 'grape', 'banana', 'strawberry', 'kiwi']
word = random.choice(word_list)

print(word_list)
print(word)

guess = input("Enter a single letter ")
if len(guess) == 1 and guess.isalpha() == True:
    print("valid input")
elif len(guess) > 2:
    print('Only one letter pls')
elif guess.isalpha() == False:
    print('Letters only please')
else:
    print('something else went wrong')