# sudoku solver with backtracking algorithm...


board = [[0,0,0,0,8,0,0,0,0],
         [8,0,9,0,7,1,0,2,0],
         [4,0,3,5,0,0,0,0,1],
         [0,0,0,1,0,0,0,0,7],
         [0,0,2,0,3,4,0,8,0],
         [7,3,0,0,0,9,0,0,4],
         [9,0,0,0,0,0,7,0,2],
         [0,0,8,2,0,5,0,9,0],
         [1,0,0,0,4,0,3,0,0]]


def findEmpty():
    for i in range(0,9):
        for j in range(0,9):
            if board[i][j]==0:
                return (i,j)
    return None


         
         
def printBoard():
    print("\n"*3)
    for i in range(1,10):
        for j in range(1,10):
            print(board[i-1][j-1],end = '')
            if j%3==0:
                print(" | ",end = '')
        print("\n",end='')
                
        if i%3==0 and i!=9:
            print("_"*17)
    print("\n"*3)
            
        
        
  

    
    
def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True




def solveSudoku():
    pos = findEmpty()
    if pos==None:
        printBoard()
        return True
    (row,col) = pos
    for no in range(1,10):
        #print ("working at position",pos)
        if valid(board,no,pos):
            board[row][col] = no
            if solveSudoku()==True:
                return True   
            board[row][col] = 0
    return False
                
            
        

printBoard()
boo = solveSudoku()
if boo:
    print("puzzle solved")
else:
    print("Sorry, this puzzle can't be solved")

        
                  
 

