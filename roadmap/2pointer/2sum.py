# %%
nums = [3, 2, 4]
target = 6
compDict = {}
for i in range(0, len(nums)):
    comp = target - nums[i]
    if nums[i] not in compDict:
        compDict[comp] = i
    else:
        print( [compDict[nums[i]], i])
        break