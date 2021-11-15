s = input()
data = ['a','e','i','o','u']

cnt = 0
for i in s:
    if i in data:
        cnt += 1

print(cnt)