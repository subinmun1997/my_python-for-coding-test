import sys

s = sys.stdin.readline().rstrip()
alpha = [0] * 26

for i in s:
    chk = int(ord(i)) - int(ord('a'))
    alpha[chk] += 1

for i in alpha:
    print(i, end=' ')