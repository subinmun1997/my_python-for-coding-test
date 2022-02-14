n = int(input())
sticks = [int(input()) for _ in range(n)]

front = sticks.pop()
count = 1

for i in range(len(sticks)-1,-1,-1):
    if sticks[i] > front:
        count += 1
        front = sticks[i]

print(count)