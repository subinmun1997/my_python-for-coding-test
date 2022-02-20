c = int(input())

max_num = 0
for _ in range(c):
    s = input()
    check = s.count('for') + s.count('while')
    max_num = max(max_num, check)

print(max_num)
