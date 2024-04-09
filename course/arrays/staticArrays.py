# %% [markdown]
"""
# Lessons:
1. For static arrays, questions don't want a new array (that's dynamic like in python)
2. Having two pointers works well, increment one over the whole array and the other when a condition is met
"""

        
# %%
nums = [0,0,1,1,1,2,2,3,3,4]
replace = 1
for i in range(1, len(nums)):
    if nums[i] != nums[i-1]:
        nums[replace] = nums[i]
        replace += 1

print(replace)
print(nums)
# %%
nums = [0,1,2,2,3,0,4,2]
val = 2
# nums = [0,1,4,0,3,_,_,_]
index = 0
for i in range(len(nums)):
    if nums[i] != val:
        nums[index] = nums[i]
        index += 1

nums
