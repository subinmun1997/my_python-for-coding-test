n = int(input())
h = list(map(int, input().split()))
a, b = divmod(sum(h), 3)
cnt = 0

if b == 0:
    for i in h:
        cnt += i//2
    if cnt >= a:
        print("YES")
    else:
        print("NO")

else:
    print("NO")
