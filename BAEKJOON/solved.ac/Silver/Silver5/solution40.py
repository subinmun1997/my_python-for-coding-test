n = int(input())
numbers = sorted(set(map(int, input().split())))
print(*numbers)
