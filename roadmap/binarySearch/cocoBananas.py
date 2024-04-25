# %%
import math
def canEat(piles, k, h):
    nHrs = 0
    for pile in piles:
        hrs = math.ceil(pile/k)
        nHrs += hrs
        if nHrs > h:
            return False

    return True

piles = [30,11,23,4,20]
h = 6
k = 2

minVal = max(piles)
potentialK = list(range(1, minVal + 1))
l, r = 0, len(potentialK) - 1
c = 0
while l <= r:
    m = (r+l) // 2

    kl = potentialK[l]
    kr = potentialK[r]
    km = potentialK[m]
    eatM = canEat(piles, km, h)

    if eatM:
        r = m - 1
        minVal = km
    else:
        l = m + 1
    c += m   
print(minVal)



# k = 4
canEat(piles, k = minVal, h = 8)