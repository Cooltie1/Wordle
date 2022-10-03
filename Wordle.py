# File: Wordle.py

import random

from WordleDictionary import FIVE_LETTER_WORDS
from WordleGraphics import WordleGWindow, N_COLS, N_ROWS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR

def wordle():
    def enter_action(s):
        #strings together the user's guess
        buildWord = ""
        for colNum in range(0,N_COLS):
            buildWord += gw.get_square_letter(gw.get_current_row(),colNum)
        
        #if the user's guess is in the dictionary, proceed
        if buildWord.lower() in FIVE_LETTER_WORDS:
            gw.show_message("You guessed " + buildWord)

            #coloring tiles

            #keeps string containing letters found
            lettersFound = ""

            #loop through tiles in current row
            for colNum in range(0,N_COLS):
                #if tile is in correct position, color green
                if gw.get_square_letter(gw.get_current_row(),colNum) == word[colNum]:
                    #add letter to list of letters found
                    lettersFound += gw.get_square_letter(gw.get_current_row(),colNum)
                    gw.set_square_color(gw.get_current_row(),colNum,CORRECT_COLOR)
            #loop through tiles in current row again
            for colNum in range(0,N_COLS):
                #if tile isn't green, but is in the word...
                if (gw.get_square_color(gw.get_current_row(),colNum) != CORRECT_COLOR) and (gw.get_square_letter(gw.get_current_row(),colNum) in word):
                    #add letter to list of letters found
                    lettersFound += gw.get_square_letter(gw.get_current_row(),colNum)
                    #if letter hasn't been found more times than it is present in the word, color it yellow
                    if lettersFound.count(gw.get_square_letter(gw.get_current_row(),colNum)) <= word.count(gw.get_square_letter(gw.get_current_row(),colNum)):
                        gw.set_square_color(gw.get_current_row(),colNum,PRESENT_COLOR)
                    #otherwise, color it grey
                    else:
                        gw.set_square_color(gw.get_current_row(),colNum,MISSING_COLOR)
                #if tile isn't green and didn't meet the first criteria (being in the word), it must be grey
                elif gw.get_square_color(gw.get_current_row(),colNum) != CORRECT_COLOR:
                    gw.set_square_color(gw.get_current_row(),colNum,MISSING_COLOR)
        #if the user's guess isn't in the dictionary, clear guess and show "not in word list" *****still need to add logic to allow another guess******
        else:
            for colNum in range(0,N_COLS):
                gw.set_square_letter(gw.get_current_row(),colNum,"")
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
