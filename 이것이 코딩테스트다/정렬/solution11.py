n = int(input())
array = [int(input()) for _ in range(n)]

array.sort(reverse=True)
print(array)