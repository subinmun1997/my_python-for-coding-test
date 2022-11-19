n = int(input())
numbers = [int(input()) for _ in range(n)]

seq = 1
stack = []
result = []
for num in numbers:
    while seq <= num:
        stack.append(seq)
        seq += 1
        result.append("+")

    if stack[-1] == num:
        stack.pop()
        result.append("-")
    else:
        print("NO")
        break
else:
    for i in result:
        print(i)