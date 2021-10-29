import sys
from collections import Counter
n = int(sys.stdin.readline())
array = []

for i in range(n):
    array.append(int(sys.stdin.readline()))

array.sort()
print(round(sum(array)//n)) # 산술평균

print(array[len(array)//2]) # 중앙값


def mode(array):
    counter = Counter(array)
    if len(counter) == 1:
        return array[0]
    counting_arr = counter.most_common(n=2)
    if counting_arr[0][1] == counting_arr[1][1]:
        return counting_arr[1][0]
    return counting_arr[0][0]

print(mode(array)) # 최빈값

print(array[-1] - array[0]) # 범위
