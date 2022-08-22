n = int(input())

def solution(n):
    def hanoi(n, start, end, mid):
        if n == 1:
            result.append([start, end])
            return
        hanoi(n - 1, start, mid, end)
        result.append([start, end])
        hanoi(n - 1, mid, end, start)

    result = []
    hanoi(n, 1, 3, 2)
    return result

result = solution(n)
print(len(result))
for x, y in result:
    print(x, y)