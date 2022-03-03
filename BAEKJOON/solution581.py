n, s, r = map(int, input().split())
damage = list(map(int, input().split()))
extra = list(map(int, input().split()))

count = s
for i in extra:
    if i in damage:
        extra.remove(i)
        damage.remove(i)
        count -= 1

for i in damage:
    for j in extra:
        if j-1 <= i <= j+1:
            extra.remove(j)
            count -= 1
            break

print(count)