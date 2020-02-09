from random import randint, seed

BOARD_SIZE = 9
"""
This module is responsible for creating the board game, 

"""

class BoardGame(object):

    def __init__(self, boardfile):
        self.board = self.__create_board(boardfile)

    def __create_board(self, boardfile):
        '''
        This helper function checks and constructs the 2D board 
        '''
        board = [] # An empty 2D array
        
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
    
