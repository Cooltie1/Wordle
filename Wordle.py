# File: Wordle.py

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

def wordle():
    def enter_action(s):
        gw.show_message("You have to implement this method.")
        

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

    #Selects random word from dictionary
    word = FIVE_LETTER_WORDS[random.randint(0,(len(FIVE_LETTER_WORDS)-1))].upper()

    letterNum = 0
    for letter in word:
        gw.set_square_letter(0,letterNum,letter)
        letterNum += 1 

# Startup code

if __name__ == "__main__":
    wordle()
