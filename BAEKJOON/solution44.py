t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    print("Case #",end='')
    print(i,end='')
    print(":",a+b)