n = int(input())
firecracker = list(map(int, input().split()))

left, right = firecracker[0], firecracker[-1]

for _ in range(n-3):
    if left > right:
        left -= 1
    else:
        right -= 1

print(max(left, right) - 1)