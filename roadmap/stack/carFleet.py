# %%
position = [10, 8, 0, 5, 3]
speed =    [2,  4, 1, 1, 3]


ps = zip(position, speed)
ps = sorted(ps, key = lambda x: x[0])
fleet = 0
