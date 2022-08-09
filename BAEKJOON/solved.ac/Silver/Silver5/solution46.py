k = int(input())

dpA = [0] * 46
dpB = [0] * 46

dpA[0] = 1
dpA[1] = 0

dpB[0] = 0
dpB[1] = 1

for i in range(2, k+1):
    dpA[i] = dpA[i-2] + dpA[i-1]
    dpB[i] = dpB[i-2] + dpB[i-1]

print(dpA[k], dpB[k])