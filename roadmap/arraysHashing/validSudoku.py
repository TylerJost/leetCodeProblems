# %%
import collections
board = [["8","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]
# %%
def isValidSudoku(board):
    cols = collections.defaultdict(list)
    rows = collections.defaultdict(list)
    squares = collections.defaultdict(list) # key = (row // 3, col //3)
    for row in range(0, 9):
        for col in range(0, 9):

            sq = (row // 3, col // 3)
            val = board[row][col]

            if val == '.':
                continue

            if val not in rows[row]:
                rows[row].append(val)
            else:
                print(f'{val} in rows')
                return cols, rows, squares, False

            if val not in cols[col]:
                cols[col].append(val)
            else:
                print(f'{val} in cols')
                return cols, rows, squares, False
            
            if val not in squares[sq]:
                squares[sq].append(val)
            else:
                print(f'{val} in squares')

                return cols, rows, squares, False
    return cols, rows, squares, True
cols, rows, squares, validity = isValidSudoku(board)

print(validity)