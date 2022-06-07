n = int(input())
tree = list(map(int, input().split()))
grow = list(map(int, input().split()))

array = []
for i in range(n):
    array.append((tree[i], grow[i]))

array.sort(key=lambda x : x[1])
answer = 0
for i in range(n):
    answer += array[i][0] + array[i][1] * i

print(answer)
