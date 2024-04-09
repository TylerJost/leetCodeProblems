# %% 682. Baseball Game
ops = ["5", "2", "C", "D", "+"]
ops = ["5","-2","4","C","D","9","+","+"]
i = 0
record = []
for op in ops:
    if op == 'D':
        record.append(record[i-1]*2)
        i += 1
    elif op == '+':
        record.append(record[i-1]+record[i-2])
        i += 1
    elif op == 'C':
        record = record[0:i-1]
        i -= 1
    else:
        record.append(int(op))
        i += 1

sum(record)
# %% 20. Valid Parentheses
s = "()[]{}"
s = "(){}(((})))]"

p = []
sb = []
cb = []
for c in s:
    if c == '(':
        p.append(c)
    elif c == '[':
        sb.append(c)
    elif c == '{':
        cb.append(c)
    
    if c == ')':
        if len(p) > 0 and p[-1] == '(':
            p.pop(-1)
        else:
            assert False, 'Parenthesis'
    if c == ']':
        if len(sb) > 0 and sb[-1] == '[':
            sb.pop(-1)
        else:
            assert False, 'Square bracket'
    if c == '}':
        if len(cb) > 0 and cb[-1] == '{':
            cb.pop(-1)
        else:
            assert False, 'Curly bracket'
# %%
