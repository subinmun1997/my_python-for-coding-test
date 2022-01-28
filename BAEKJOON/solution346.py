n = int(input())
answer = list(map(int, input().split()))

result = 0
first = 1
for a in answer:
    if a == 1:
        result += first
        first += 1
    else:
        first = 1

print(result)