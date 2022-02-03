n = int(input())
s = input()
count_two = s.count('2')
count_e = s.count('e')

if count_two > count_e:
    print("2")
elif count_two < count_e:
    print("e")
else:
    print("yee")