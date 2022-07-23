n = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())), reverse=True)

result = 0
for i in range(n):
    result += A[i] * B[i]

print(result)