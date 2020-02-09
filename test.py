board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]
BOARD = 9

def draw(boardfile):

    puzzle = []
    for i in range(len(boardfile)):
        if i % 3 == 0 and i != 0 :
            print("- - - - - - - - - - - - - ")
        for j in range(len(boardfile)):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")       
            
            if j == 8:
                print(boardfile[i][j])
            else:
                print(str(boardfile[i][j]) + " ", end="")

def find_empty(boardfile):
    empty_ = []
    for i in range(len(boardfile)):
        for j in range(len(boardfile)):
            if boardfile[i][j] == 0:
                empty_.append((i, j)) # returns all empty positions
    
    return empty_

#TODO Create a model tha populates the empty spots with potential numbers




print(find_empty(board))