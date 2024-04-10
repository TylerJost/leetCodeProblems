# %%
temperatures = [73,74,75,71,69,72,76,73]
temperatures = [30,40,50,60]
temperatures = [30,60,90]
nex = 0
outs = []
for cur in range(0, len(temperatures)):
    nex = cur + 1
    dayWait = 0
    while nex < len(temperatures):
        if temperatures[nex] > temperatures[cur]:
            dayWait = nex - cur
            break
        nex += 1
    outs.append(dayWait)
        
print(outs)