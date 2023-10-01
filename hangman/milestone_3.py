import milestone_2

def check_guess(guess):
  guess = guess.lower()
  if guess in milestone_2.word:
    print(f"Good guess {guess} is in the word")    
  else:
    print(f"Sorry, {guess} is not in the word. Try again.")

def ask_for_input():
  
  while True:
    guess = input("please input a letter ")  
    if len(guess) == 1 and guess.isalpha():
      print("Good guess")
      break  
    elif len(guess) != 1:
      print("Oops! That is not a valid input. Input is greater than one letter")
      #raise ValueError
    elif guess.isalpha() == False:
      print("Oops! That is not a valid input. Input is not a letter")  
      #raise TypeError
  check_guess(guess)
  

ask_for_input()
