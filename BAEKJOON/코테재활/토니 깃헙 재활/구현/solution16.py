n = int(input())
switch = [-1] + list(map(int, input().split()))

def change(num):
    switch[num] = 1 - switch[num]

m = int(input())
for _ in range(m):
    x, y = map(int, input().split())
    if x == 1:
        for i in range(y, n+1, y):
            change(i)
    else:
        change(y)
        for k in range(n//2):
            if y + k > n or y - k < 1:
                break
            if switch[y+k] == switch[y-k]:
                change(y+k)
                change(y-k)
            else:
                break

for i in range(1, n+1):
    print(switch[i], end=' ')
    if i%20 == 0:
        print()