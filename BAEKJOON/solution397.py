month = int(input())
day = int(input())

if month == 1 or (month <= 2 and day < 18):
    print("Before")
elif month == 2 and day == 18:
    print("Special")
else:
    print("After")