t = int(input())

def move_array(array, n, d):
    total = abs(d) // 45
    if d > 0:
        change = n // 2
        for k in range(total):
            temp = [[0] * n for _ in range(n)]
            for i in range(n):
                temp[i][change] = array[i][i]

            for i in range(n):
                temp[i][(n - 1) - i] = array[i][change]

            for i in range(n):
                temp[change][i] = array[(n - 1) - i][i]

            for i in range(n):
                temp[i][i] = array[change][i]

            for i in range(n):
                for j in range(n):
                    if temp[i][j] == 0:
                        temp[i][j] = array[i][j]
            array = temp

    else:
        change = n // 2
        for k in range(total):
            temp = [[0] * n for _ in range(n)]

            for i in range(n):
                temp[change][i] = array[i][i]

            for i in range(n):
                temp[(n - 1) - i][i] = array[change][i]

            for i in range(n):
                temp[(n - 1) - i][change] = array[(n - 1) - i][1]

            for i in range(n):
                temp[(n - 1) - i][(n - 1) - i] = array[(n - 1) - i][change]

            for i in range(n):
                for j in range(n):
                    if temp[i][j] == 0:
                        temp[i][j] = array[i][j]

            array = temp

    return temp

for _ in range(t):
    n, d = map(int, input().split())
    array = [list(map(int, input().split())) for _ in range(n)]
    new_array = move_array(array, n, d)

    for i in new_array:
        print(*i)