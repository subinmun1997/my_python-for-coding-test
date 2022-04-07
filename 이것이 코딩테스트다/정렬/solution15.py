n = int(input())
house = sorted(list(map(int, input().split())))

print(house[(n-1)//2]) # 중앙값