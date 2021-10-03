m = int(input())
n = int(input())

a = []

for i in range(m, n+1):
    is_sosu = False
    if i == 2:
        a.append(i)
    for j in range(2,int(i**0.5)+1):
        if i%j == 0:
            is_sosu = False
            break
        else:
            is_sosu = True
            continue
    if is_sosu:
        a.append(i)

print(sum(a), min(a), sep='\n') if len(a) > 0 else print(-1)
