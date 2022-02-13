n = int(input())
dot = [0, 5, 12, 22] #1단계, 2단계, 3단계

if n <= 3:
    print(dot[n])
else:
    mul = 0
    for i in range(n-1):
        mul += (7+3*i)
    print((5+mul)%45678)
