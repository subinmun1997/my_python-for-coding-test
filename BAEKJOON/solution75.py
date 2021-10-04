x, y, w, h = map(int, input().split())

result = min(x,y,h-y,w-x)
print(result)
