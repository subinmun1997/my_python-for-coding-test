n, m = map(int, input().split()) # 스크린, 바구니
j = int(input())
location = [int(input()) for _ in range(j)]

left = 1
right = m

move_count = 0
for loc in location:
    if right < loc:
        move_count += loc - right
        right = loc
        left = loc - m + 1
    elif left > loc:
        move_count += left - loc
        left = loc
        right = loc + m -1

print(move_count)