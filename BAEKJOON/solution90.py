x, y = map(int, input().split())

days = 0
for i in range(1,x):
    if i in [1,3,5,7,8,10,12]:
        days += 31
    elif i in [4,6,9,11]:
        days += 30
    else:
        days += 28

days += y

day_table = ["SUN","MON","TUE","WED","THU","FRI","SAT"]

for j in range(7):
    if (days % 7 == j):
        print(day_table[j])


