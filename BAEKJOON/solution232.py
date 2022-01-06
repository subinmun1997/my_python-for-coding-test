n = int(input())

check = [False]+[True]*103
p = []
s = []

for i in range(2, 104):
    if check[i]:
        p.append(i)
        for j in range(2*i,104,i):
            check[j] = False

for i in range(1, len(p)):
    s.append(p[i]*p[i-1])

for i in s:
    if i>n:
        print(i)
        break