def sum_k(k):
    add_k = 0
    for i in range(1, k+1):
        add_k += i
    return add_k

def trianlge(n):
    value = 0
    for k in range(1, n+1):
        value += k * sum_k(k+1)
    return value

t = int(input())

for _ in range(t):
    n = int(input())
    answer = trianlge(n)
    print(answer)