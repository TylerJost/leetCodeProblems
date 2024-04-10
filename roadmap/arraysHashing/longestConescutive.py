# %%
nums = [0,3,7,2,5,8,4,6,0,1, 100, 101 , 102, 103]
def longestConsecutive(nums) -> int:
    numsSet = set(nums)
    seqLen = 0
    seqMax = 0
    for num in nums:
        if num - 1 not in numsSet:
            seqLen = 1
            while True:
                if num+1 in numsSet:
                    seqLen += 1
                    num += 1
                else:
                    break
            if seqLen > seqMax:
                seqMax = seqLen
    return seqMax

longestConsecutive(nums)

