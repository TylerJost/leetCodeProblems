nums = [-1,0,3,5,9,12]
target = 12
L, R = 0, len(nums) - 1
idx = len(nums) + 1
while L <= R:
    mid = (L + R) //2

    if nums[mid] < target:
        L = mid + 1
    elif nums[mid] > target:
        R = mid - 1
    else:
        idx = mid
        break

if idx == len(nums) + 1:
    idx = -1
print(idx)