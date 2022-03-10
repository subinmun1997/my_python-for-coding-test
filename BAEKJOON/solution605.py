n = int(input())
arr = list(map(int, input().split()))

arr.sort(reverse=True)

gold = 0
for i in arr[1:]:
    gold += arr[0] + i

print(gold)