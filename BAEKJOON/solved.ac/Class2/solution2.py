x, y, w, h = map(int, input().split())

temp = [h-y, w-x, x, y]
print(min(temp))