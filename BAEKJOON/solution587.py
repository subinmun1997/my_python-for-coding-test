x, y = map(int, input().split()) # 온기, 수분

print(x+y+(min(x, y) // 10))