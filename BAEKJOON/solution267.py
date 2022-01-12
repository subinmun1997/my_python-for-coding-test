n = int(input())
place = input()
l_place = place.count('LL')
s_place = n - (l_place * 2)
total = l_place + s_place

cup_holder = total + 1
if n < cup_holder:
    print(n)
else:
    print(cup_holder)