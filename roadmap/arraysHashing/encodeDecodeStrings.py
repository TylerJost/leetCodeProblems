# %%
message = ['lint', 'code', 'love', 'you']

# You can't just make a complicated delimeter for this problem
# Strategy: put in the number of letters followed by a delimeter (@) 
# [4@lint4@code4@love3@you]
def encode(strs):
    encoded = ''
    for word in strs:
        wordLen = len(word)
        encoded += f'{wordLen}@{word}'
    return encoded
def decode(s):
    message = []
    i = 0
    while i < len(s):
        wordLen = int(s[i])
        message.append(s[i+2:i+2+wordLen])

        i += 2+wordLen
        print(message)
    return message
# %%

message = ["we","say",":","yes","!@#$%^&*()"]
encoded = encode(message)

decoded = decode(encoded)
# %%
s = encoded
message = []
i = 0
while i < len(s):
    wordLen = ''
    while s[i] != '@':
        wordLen += s[i]
        i += 1
    wordLen = int(wordLen)
    message.append(s[i+1:i+1+wordLen])

    i += 1+wordLen
    print(message)