# %%
nums = [1, 2 , 3, 2, 3, 3, 3]
k = 4

window = set()
L = 0
for R in range(len(nums)):
    if R - L + 1 > k:
        window.remove(nums[L])
        L += 1
    if nums[R] in window:
        print('True')
        break
    window.add(nums[R])
    print(f'{L} {R} {window}')