import math
import sys

l = int(sys.stdin.readline())
s = sys.stdin.readline().rstrip()

total = 0
for i in range(l):
    total += (ord(s[i]) - 96) * (31 ** i)

print(total % 1234567891)