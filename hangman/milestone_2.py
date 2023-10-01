import random
word_list = ["apple", "pear", "banana", "satsuma", "mango"]
print(word_list)

word = random.choice(word_list)
print(word)

# for i in range(0,5):
#   word = random.choice(word_list)
#   print(word)
# guess = input("please input a letter ")  
# if len(guess) == 1 and guess.isalpha():
#   print("Good guess")
# elif len(guess) != 1:
#   print("Oops! That is not a valid input. Input is greater than one letter")
#   raise ValueError
# elif guess.isalpha() == False:
#   print("Oops! That is not a valid input. Input is not a letter")  
#   raise TypeError
# print(guess)