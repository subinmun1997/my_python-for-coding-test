from collections import deque

n, m = map(int, input().split())
idx = list(map(int, input().split()))
nums = deque([i for i in range(1, n+1)])

result = 0
for i in idx:
    if nums[0] == i:
        nums.popleft()
    else:
        if nums.index(i) < len(nums) - nums.index(i):
            while nums[0] != i:
                nums.append(nums.popleft())
                result += 1
            nums.popleft()

        else:
            while nums[0] != i:
                nums.appendleft(nums.pop())
                result += 1
            nums.popleft()

print(result)