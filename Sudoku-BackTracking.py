board = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]
def valid(bo, num, pos):
    #Check Row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
    for j in range(len(bo)):
        if bo[j][pos[1]] == num and pos[0] != j:
            return False
    #Check 3x3 cube
    box_X,box_Y = pos[1] // 3, pos[0] // 3
    for i in range(box_Y*3, box_Y*3+3):
        for j in range(box_X*3, box_X*3+3):
            if bo[i][j] == num and i != pos[0] and j != pos[1]:
                return False
    return True

def solve(bo):
    find = find_empty(bo)
    if find == -1:
        return True
    else:
        row, col = find
    
    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True
            
            bo[row][col] = 0
    return False
    
    
def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i !=0:
            print('- - - - - - - - - - - -')
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            print(str(bo[i][j]) + " ", end="")
            if j == 8:
                print()

def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i,j)
    else:
         return -1   
    
print_board(board)
print()
solve(board)
print()
print_board(board)