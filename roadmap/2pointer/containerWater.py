# %%
height = [1, 11, 6, 2, 5, 4, 11, 3, 7]

L = 0
R = len(height) - 1
maxArea = 0
while True:
    hL = height[L]
    hR = height[R]
    area = (min([hL,hR])) * (R - L)
    
    if area > maxArea:
        maxArea = area

    if height[L+1] > height[R-1]:
        L += 1
    else:
        R -= 1
    
    if L == R:
        break

print(maxArea)