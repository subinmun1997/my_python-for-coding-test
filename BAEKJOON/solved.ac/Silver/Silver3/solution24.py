import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
number = sorted([int(input()) for _ in range(n)])

print(round(sum(number)/n))
print(number[n//2])

def mode(arr):
    counter = Counter(arr)
    if len(counter) == 1:
        return arr[0]
    counting_arr = counter.most_common(n=2)
    if counting_arr[0][1] == counting_arr[1][1]:
        return counting_arr[1][0]
    return counting_arr[0][0]

print(mode(number))

print(number[-1] - number[0])

