melody = list(map(int, input().split()))

asc = sorted(melody)
des = sorted(melody, reverse=True)

if melody == asc:
    print("ascending")
elif melody == des:
    print("descending")
else:
    print("mixed")