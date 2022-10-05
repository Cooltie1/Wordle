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
            #coloring tiles

            #keeps string containing letters found
            lettersFound = ""

            #loop through tiles in current row
            for colNum in range(0,N_COLS):
                #if tile is in correct position, color TILE and KEY green
                if gw.get_square_letter(gw.get_current_row(),colNum) == word[colNum]:
                    #add letter to list of letters found
                    lettersFound += gw.get_square_letter(gw.get_current_row(),colNum)
                    gw.set_square_color(gw.get_current_row(),colNum,CORRECT_COLOR)
                    gw.set_key_color(gw.get_square_letter(gw.get_current_row(),colNum),CORRECT_COLOR)
            #loop through tiles in current row again
            for colNum in range(0,N_COLS):
                #if TILE isn't green, but is in the word...
                if (gw.get_square_color(gw.get_current_row(),colNum) != CORRECT_COLOR) and (gw.get_square_letter(gw.get_current_row(),colNum) in word):
                    #add letter to list of letters found
                    lettersFound += gw.get_square_letter(gw.get_current_row(),colNum)
                    #if letter hasn't been found more times than it is present in the word, color TILE yellow
                    if lettersFound.count(gw.get_square_letter(gw.get_current_row(),colNum)) <= word.count(gw.get_square_letter(gw.get_current_row(),colNum)):
                        gw.set_square_color(gw.get_current_row(),colNum,PRESENT_COLOR)
                    #otherwise, color TILE grey
                    else:
                        gw.set_square_color(gw.get_current_row(),colNum,MISSING_COLOR)
                    #if KEY isn't green already, color it yellow
                    if gw.get_key_color(gw.get_square_letter(gw.get_current_row(),colNum)) != CORRECT_COLOR:
                        gw.set_key_color(gw.get_square_letter(gw.get_current_row(),colNum), PRESENT_COLOR)
                #if TILE isn't green and didn't meet the first criteria (being in the word), TILE and KEY must be grey
                elif gw.get_square_color(gw.get_current_row(),colNum) != CORRECT_COLOR:
                    gw.set_square_color(gw.get_current_row(),colNum,MISSING_COLOR)
                    gw.set_key_color(gw.get_square_letter(gw.get_current_row(),colNum), MISSING_COLOR)
            #display congratulations if guess is correct
            if buildWord == word:
                gw.show_message("Congratulations! You guessed the word!")
            #display incorrect message and reveal word if last guess is incorrect
            elif gw.get_current_row() == N_ROWS - 1:
                gw.show_message("Game over! The word was " + word + ".")
            #display message to keep guessing if guess is incorrect
            else:
                gw.show_message("Your guess, " + buildWord + ", is incorrect. Keep guessing!")
            #move to next row to allow another guess unless game is over
            if gw.get_current_row() < (N_ROWS - 1):
                gw.set_current_row(gw.get_current_row() + 1)
        #if the user's guess isn't in the dictionary, clear guess and show "not in word list"
        else:
            for colNum in range(0,N_COLS):
                gw.set_square_letter(gw.get_current_row(),colNum,"")
            gw.show_message("Not in word list.")
            gw.set_current_row(gw.get_current_row())
        

    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)

    #Selects random word from dictionary
    word = FIVE_LETTER_WORDS[random.randint(0,(len(FIVE_LETTER_WORDS)-1))].upper()

    #moves to first row to allow user's first guess
    gw.set_current_row(0)

# Startup code
if __name__ == "__main__":
    wordle()