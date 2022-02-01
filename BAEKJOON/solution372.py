n, m = map(int, input().split())
check = ''
for _ in range(n):
    check += str(n)

if int(check) <= 2016:
    print(check)
else:
    print(check[:m])