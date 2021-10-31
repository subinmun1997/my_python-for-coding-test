import sys

for i in range(int(sys.stdin.readline())):
    a, b = map(int, input().split())
    c = pow(a, b, 10) # pow(a, b) % 10
    if c:
        print(c)
    else:
        print(10)


