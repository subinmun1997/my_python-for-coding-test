n = int(input())
array = [int(input()) for _ in range(n)]

stack = []
result = []
temp = []

num = 1
for i in array:
    while num <= i:
        stack.append(num)
        result.append("+")
        num += 1
    if stack:
        if stack[-1] == i:
            temp.append(stack.pop())
            result.append("-")

if temp == array:
    for i in result:
        print(i)
else:
    print("NO")