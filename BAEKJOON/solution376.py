data = list(map(int, input().split()))
sort_data = sorted(data)

if data == sort_data:
    print("Good")
else:
    print("Bad")