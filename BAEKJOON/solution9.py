n = int(input())
data = [int(input()) for _ in range(n)]
value = max(data)

stack = []
result = []
tmp = []
num = 1
for i in data: # 4 3 6 8 7 5 2 1
    while num <= i:
        stack.append(num)
        result.append("+")
        num += 1
    if len(stack) > 0:
        if i == stack[-1]:
            tmp.append(stack.pop())
            result.append("-")
if tmp == data:
    for i in result:
        print(i)
else:
    print("NO")