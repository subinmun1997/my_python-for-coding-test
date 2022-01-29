a, b = map(int, input().split())

min_value = min(a, b)
max_value = max(a, b)

diff = max_value - min_value - 1
if max_value == min_value or min_value+1 == max_value:
    diff = 0
print(diff)
for i in range(min_value+1, max_value):
    print(i, end=' ')