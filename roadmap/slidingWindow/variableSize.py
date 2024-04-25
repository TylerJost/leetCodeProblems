# %%
nums = [2, 3, 1, 2, 4, 3]
target = 6

L, total = 0, 0
length = len(nums) + 1
for R in range(len(nums)):
    total += nums[R]

    # Here's where it gets tricky
    # We want to move the left pointer forward (shrinking the total)
    # But we want to only do this while we're greater than the target
    while total >= target:

        length = min(R - L + 1, length)
        total -= nums[L]
        L += 1


    
print(f'Length: {length}')

# %% Binary search (practice)
# Given an array of integers nums which is sorted in ascending order, 
# and an integer target, write a function to search target in nums. 
#If target exists, then return its index. Otherwise, return -1.
