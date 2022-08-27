from collections import Counter

n = int(input())
num = sorted(int(input()) for _ in range(n))

print(round(sum(num)/n))
print(num[n//2])

def mode(arr):
    counter = Counter(arr)
    if len(counter) == 1:
        return arr[0]
    counting_arr = counter.most_common(2)
    if counting_arr[0][1] == counting_arr[1][1]:
        return counting_arr[1][0]
    return counting_arr[0][0]

print(mode(num))
print(num[-1] - num[0])