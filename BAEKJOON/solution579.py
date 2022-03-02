n, l, k = map(int, input().split())
questions = []

for _ in range(n):
    sub1, sub2 = map(int, input().split())
    questions.append((sub1, sub2))

questions.sort(key=lambda x : x[1])

easy = hard = 0
for x, y in questions:
    if k == 0:
        break
    if l >= y:
        hard += 1
        k -= 1
    elif l >= x:
        easy += 1
        k -= 1

result = hard * 140 + easy * 100
print(result)