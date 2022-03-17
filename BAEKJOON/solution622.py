n, k = map(int, input().split())
location = list(input())

count = 0
for i in range(n):
    if location[i] == 'P':
        for j in range(i-k, i+k+1):
            if 0 <= j < n and location[j] == 'H':
                count += 1
                location[j] = "0"
                break

print(count)