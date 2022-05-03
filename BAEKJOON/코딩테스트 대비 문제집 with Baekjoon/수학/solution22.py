import sys

input = sys.stdin.readline
a, b = map(int, input().split())

prime = [False, False] + [True] * 10000000
cnt = 0
for i in range(2, 10000001):
    if prime[i]:
        t = 2
        while True:
            if i ** t > b:
                break
            if a <= i**t <= b:
                cnt += 1
            t += 1
        for j in range(2*i, 10000001, i):
            prime[j] = False

print(cnt)