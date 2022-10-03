# File: Wordle.py

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def wordle():
    def enter_action(s):
        currentRow = gw.get_current_row()
        buildWord = ""
        for tile in range(0,N_COLS):
            buildWord += gw.get_square_letter(currentRow,tile)
        if buildWord.lower() in FIVE_LETTER_WORDS:
            gw.show_message("You guessed " + buildWord)

            #method 1 for coloring tiles
            lettersFound = ""
            for letterNum in range(0,N_COLS):
                if gw.get_square_letter(gw.get_current_row(),letterNum) == word[letterNum]:
                    gw.set_square_color(gw.get_current_row(),letterNum,CORRECT_COLOR)
                    lettersFound += gw.get_square_letter(gw.get_current_row(),letterNum)
                elif (gw.get_square_letter(gw.get_current_row(),letterNum) in word) and (lettersFound.count(gw.get_square_letter(gw.get_current_row(),letterNum)) <= word.count(gw.get_square_letter(gw.get_current_row(),letterNum))):
                    gw.set_square_color(gw.get_current_row(),letterNum,PRESENT_COLOR)
                    lettersFound += gw.get_square_letter(gw.get_current_row(),letterNum)
                else:
                    gw.set_square_color(gw.get_current_row(),letterNum,MISSING_COLOR)
            
            # #method 2 for coloring tiles
            # letterNum = 0
            # for letter in word:
            #     if gw.get_square_letter(gw.get_current_row(),letterNum) == letter:
            #         gw.set_square_color(gw.get_current_row(),letterNum,CORRECT_COLOR)
            #     elif gw.get_square_letter(gw.get_current_row(),letterNum) in word:
            #         gw.set_square_color(gw.get_current_row(),letterNum,PRESENT_COLOR)
            #     else:
            #         gw.set_square_color(gw.get_current_row(),letterNum,MISSING_COLOR)
            #     letterNum += 1
        else:
            for tile in range(0,N_COLS):
                gw.set_square_letter(currentRow,tile,"")
            gw.show_message("Not in word list.")
        

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

    #Selects random word from dictionary
    word = "GLASS"
    #word = FIVE_LETTER_WORDS[random.randint(0,(len(FIVE_LETTER_WORDS)-1))].upper()

    letterNum = 0
    for letter in word:
        gw.set_square_letter(0,letterNum,letter)
        letterNum += 1

    gw.set_current_row(1)

# Startup code

if __name__ == "__main__":
    wordle()
