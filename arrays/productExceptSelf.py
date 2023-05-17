# %%
nums = [1,2,3,4]
   
# Get prefix
prefix = [nums[0]]
for num in range(1,len(nums)):
    prefix.append(prefix[num-1]*nums[num])
# Get postfix
postfix = [nums[-1]]
current = nums[-1]
for num in range(len(nums)-2, -1, -1):
    post = nums[num]*current
    postfix.append(post)
    current = post
postfix = postfix[::-1]
# Append for output
prefix = [1] + prefix +[1]
postfix = [1] + postfix + [1]

output = []
for num in range(1, len(postfix)-1):
    output.append(prefix[num-1]*postfix[num+1])
print(output)
