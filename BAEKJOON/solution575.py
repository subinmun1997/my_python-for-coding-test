n, m = map(int, input().split())
box = list(map(int, input().split()))
book = list(map(int, input().split()))

tresh = 0
i = j = 0
while i < n and j < m:
    if book[j] <= box[i]:
        box[i] -= book[j]
        j += 1
    else:
        tresh += box.pop(i)

print(sum(box) + tresh)