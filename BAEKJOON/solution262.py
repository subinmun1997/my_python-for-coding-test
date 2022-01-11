import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n = int(input())
    tele = [input().rstrip() for _ in range(n)]
    tele.sort()

    for i in range(n-1):
        length = len(tele[i])
        if tele[i] == tele[i+1][:length]:
            print("NO")
            break
    else:
        print("YES")
