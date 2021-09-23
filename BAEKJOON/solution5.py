import sys
n = int(sys.stdin.readline())

array = [list(map(int, input().split())) for i in range(n)]
result = 1
array = sorted(array, key=lambda a: (a[1], a[0])) # 같은 end_time 이라면 start_time 순으로 재정렬

x, y = array[0]

for i in range(1,len(array)):
    if y <= array[i][0]:
        result += 1
        y = array[i][1]

print(result)