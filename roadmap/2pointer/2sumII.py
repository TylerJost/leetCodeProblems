# %%
"""
numbers = [2, 3, 7, 11, 15]
target = 10
Start with pointers on each end

2 + 15 > 10 --> Can't be 15, so move right pointer
2 + 11 > 10 --> Move right pointer
2 + 7  < 10 --> Move left pointer

"""
# %%
numbers = [2, 3, 7, 11, 15]
target = 10

L = 0
R = len(numbers) - 1

while True:
    nL = numbers[L]
    nR = numbers[R]

    if nL + nR > target:
        R -= 1
    elif nL + nR < target:
        L += 1
    elif nL + nR == target:
        print(L+1, R+1)
        break