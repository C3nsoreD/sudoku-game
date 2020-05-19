"""
Testing the board game generator that will generate board games for testing the solver algorithms. 

"""
from .gamelogic import Game 
from .sudokuboard import BoardGame

""" Create a sudoku game board """

def shift_row(array, n):        
    return array[n:] + array[:n]


def print_2d(array):
    for row in array:
        for col in row:
            print(col, end=" ")
        print()


def main():
    empty_board = [[]] * 9
    base_row = random.sample(range(1, 10), 9) # Row that is used to initialize the board        

    empty_board[0] = base_row

    #  group filling and circular shift:
    for i in range(len(empty_board)):
        if i == len(empty_board) - 1:
            break
        if i == 3:
            empty_board[i+1] = shift_row(empty_board[i], 1)
        if i == 6:
            empty_board[i+1] = shift_row(empty_board[i], 1)
        else:
            empty_board[i+1] = shift_row(empty_board[i], 3)

    np.random.shuffle(empty_board) # np.random.shuffle shuffles the 



if __name__ == "__main__":
    main()
