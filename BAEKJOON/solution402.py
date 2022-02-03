import sys
input = sys.stdin.readline

q = int(input())

square = [2**i for i in range(0, 31)]

for _ in range(q):
    n = int(input())
    print(1 if n in square else 0)