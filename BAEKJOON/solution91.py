data = list(map(int, input().split()))

asc = sorted(data)
des = sorted(data, reverse=True)

if data == asc:
    print("ascending")
elif data == des:
    print("descending")
else:
    print("mixed")