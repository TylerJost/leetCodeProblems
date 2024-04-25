# %%
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3

L, R = 0, len(matrix)-1
row = -1
while L < R:
    M = (R + L) // 2
    if matrix[M][0] <= target and matrix[M][-1] >= target:
        row = M
        break
    
    if matrix[M][0] > target:
        R = M - 1
    elif matrix[M][0] < target:
        L = M + 1
    else:
        sol = True


print(row)
