n = int(input())
number = sorted([int(input()) for _ in range(n)], reverse=True)

for i in number:
    print(i)
