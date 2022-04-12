import sys
input = sys.stdin.readline

n = int(input())
circle = []
stack = []

for i in range(n):
    data = list(map(int, input().split()))
    a = data[0] - data[1]
    b = data[0] + data[1]
    circle.append([a, i, 0])
    circle.append([b, i, 1])

circle.sort()

for i in range(n):
    first = circle[i][2]
    if first == 0:
        stack.append(circle[i])
    else:
        if stack[-1][2] == 0:
            if stack[-1][1] == circle[i][1]:
                stack.pop()
            else:
                print("NO")
                exit(0)

print("YES")
