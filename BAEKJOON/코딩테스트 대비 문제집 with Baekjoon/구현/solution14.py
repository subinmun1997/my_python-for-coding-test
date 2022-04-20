n = int(input())
switch = list(map(int, input().split()))
switch.insert(0, -1)

def change(num):
    if switch[num] == 1:
        switch[num] = 0
    else:
        switch[num] = 1

student = int(input())
for _ in range(student):
    sex, num = list(map(int, input().split()))
    if sex == 1:
        for i in range(num, n+1, num):
            change(i)
    else:
        change(num)
        for k in range(n//2):
            if num + k > n or num - k < 1:
                break
            if switch[num+k] == switch[num-k]:
                change(num+k)
                change(num-k)
            else:
                break

for i in range(1, n+1):
    print(switch[i], end=' ')
    if i%20 == 0:
        print()