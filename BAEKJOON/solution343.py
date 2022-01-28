n = int(input())

for i in range(n):
    if i%2 == 0:
        print("* " * (n-1),end='')
        print("*")
    else:
        print(" *" * n)