import random, sys

class Hangman:
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives (=5) and a random word from the word_list.

    
    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_letters: list
        A list of the letters that have already been tried

    Methods:
    -------
    check_letter(letter)
        Checks if the letter is in the word.
    ask_letter()
        Asks the user for a letter.
    '''
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = ["_" for i in self.word]
        self.num_letters = len(''.join(set(self.word)))
        self.num_lives = num_lives
        
        self.list_letters = []

        # 1. "The mystery word has {num_letters} characters"
        # 2. {word_guessed}
        print(f"The mystery word has {self.num_letters} unique characters")
        print(self.word_guessed)
        pass

    def check_letter(self, letter) -> None:
        '''
        Checks if the letter is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.

        Parameters:
        ----------
        letter: str
            The letter to be checked

        '''
        # Convert the letter to lowercase
        letter = letter.lower()
        if letter in self.word:
            # print(f"Good guess, letter {letter} is in the word")
            # Get the indices of the guessed letter
            letter_indices = [pos for pos, char in enumerate(self.word) if char == letter]
            for index in letter_indices:
                self.word_guessed[index] = letter  
            # Reduce the number of unique letters that haven't been guessed    
            self.num_letters -= 1       
            if self.num_letters == 0:
                print("Congratulations! You won!")
                sys.exit(0)
                return
            print(self.word_guessed)
        else:
            self.num_lives -= 1 
            print(f"Sorry, {letter} is not in the word.")
            print(f"You have {self.num_lives} lives remaining. Try again.")  
            if self.num_lives == 0:
                print(f"You lost! The word was {self.word}")
                sys.exit(0)
                return               
        pass

    def ask_letter(self):
        '''
        Asks the user for a letter and checks two things:
        1. If the letter has already been tried
        2. If the character is a single character
        If it passes both checks, it calls the check_letter method.
        '''
        while True:
            
            letter = input("please input a letter ")  
            if letter in self.list_letters:
                print(f"{letter} was already tried")
                continue
            elif len(letter) == 1 and letter.isalpha():
                self.list_letters.append(letter)
                break  
            elif len(letter) != 1:
                print("Please, enter just one character")
                #raise ValueError
                continue
            elif letter.isalpha() == False:
                print("Oops! That is not a valid input. Input is not a letter")  
                #raise TypeError
                continue
        self.check_letter(letter)

        pass

def play_game(word_list):
    # Initalise a Hangman object
    game = Hangman(word_list, num_lives=5)

    while True:
        game.ask_letter()        

    pass

if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)
# %%
