l, p = map(int, input().split())
c = list(map(int, input().split()))

value = l * p
for i in c:
    print(i - value, end=' ')