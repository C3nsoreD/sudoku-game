import random
import numpy as np


BOARD_SIZE = 9
""" Randomly generates sudoku game boards
"""

class BoardGameGenerator:
    def __init__(self):
        pass

    def __create_board(self):
        '''
        This helper function checks and constructs the 2D array that will contain the board game
        '''
        board = [] 
        
        # Each line must satisfy game conditions. i.e only 9 numbers, doesnot check if the board is valid
        for line in boardfile:
            line = line.strip() # create a list of the elements
            if len(line) != BOARD_SIZE:
                raise GameError("There must be 0-9 numbers in a row")
            
            board.append([]) # Create an empty 2D board 
            
            # Checks charaters
            for c in line:
                if not c.isdigit():
                    raise GameError("Only numbers 1-9 allowed")
                
                board[-1].append(int(c))

        if len(board) != 9:
            raise GameError("The board has to have 9 rows")
        return board

    # Add generator functiono 
