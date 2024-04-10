# %%
"""


"""
# %%
nums = [-1,0,1,2,-1,-4]

nums = sorted(nums)

# Two problem?
triple = []
target = 0
used = []
for fix in range(0, len(nums)):
    L = 0
    R = len(nums) - 1
    nF = nums[fix]


    while True:

        if L == fix:
            L += 1
        elif R == fix:
            R -= 1

        if L >= R:
            break

        nL = nums[L]
        nR = nums[R]

        if nL + nR + nF > target:
            R -= 1 
        elif nL + nR + nF < target:
            L += 1
        elif nL + nR + nF == target:
            triple.append([nL, nR, nF])
            used += [nL, nR, nF]
            break

print(triple)