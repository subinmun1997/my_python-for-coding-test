n, m, k = map(int, input().split())
nums = sorted(list(map(int, input().split())), reverse=True)

first = nums[0]
second = nums[1]

first_time = (m // (k+1) * k + m % (k+1))

result = first * first_time + second * (m - first_time)
print(result)
