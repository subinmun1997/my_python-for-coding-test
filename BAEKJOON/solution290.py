n = int(input())

array = []
answer = [0 for _ in range(1000)]

for i in range(n):
    d, w = map(int, input().split())
    array.append((d,w))

array.sort(reverse=True, key=lambda x : x[1])

for i in range(n):
    for j in range(array[i][0]-1, -1, -1):
        if answer[j] == 0:
            answer[j] = array[i][1]
            break

print(sum(answer))