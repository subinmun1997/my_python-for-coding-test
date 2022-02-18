max_h = 1
max_l = 0

n = int(input())
stack = []

for _ in range(n):
    l, h = map(int, input().split())
    stack.append([l, h])
    if max_l < l:
        max_l = l
    if max_h < h:
        max_h = h
        max_index = l

stack_list = [0] * (max_l + 1)
for l, h in stack:
    stack_list[l] = h

total = 0
temp = 0
for i in range(max_index+1):
    if stack_list[i] > temp:
        temp = stack_list[i]
    total += temp

temp = 0
for i in range(max_l, max_index, -1):
    if stack_list[i] > temp:
        temp = stack_list[i]
    total += temp

print(total)