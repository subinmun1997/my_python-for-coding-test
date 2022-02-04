n = int(input())

for _ in range(n):
    x = input()
    if x[len(x)//2-1] == x[len(x)//2]:
        print("Do-it")
    else:
        print("Do-it-Not")