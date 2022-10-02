# File: Wordle.py

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS

def wordle():
    def enter_action(s):
        currentRow = gw.get_current_row()
        buildWord = ""
        for tile in range(0,N_COLS):
            buildWord += gw.get_square_letter(currentRow,tile)
        if buildWord.lower() in FIVE_LETTER_WORDS:
            gw.show_message("You guessed " + buildWord)
        else:
            for tile in range(0,N_COLS):
                gw.set_square_letter(currentRow,tile,"")
            gw.show_message("Not in word list.")
        

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

    #Selects random word from dictionary
    word = FIVE_LETTER_WORDS[random.randint(0,(len(FIVE_LETTER_WORDS)-1))].upper()

    letterNum = 0
    for letter in word:
        gw.set_square_letter(0,letterNum,letter)
        letterNum += 1

    gw.set_current_row(1)




# Startup code

if __name__ == "__main__":
    wordle()
