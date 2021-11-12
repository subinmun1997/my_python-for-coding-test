n = int(input())

array = [input() for _ in range(n)]
array_len = len(array[0])

ans = ['0' for _ in range(array_len)]
if n == 1:
    ans = [i for i in array]

else:
    for i in range(1, n):
        for j in range(array_len):
            if array[0][j] != array[i][j]:
                ans[j] = '?'
            elif ans[j] != '?':
                ans[j] = array[0][j]

print(''.join(ans))