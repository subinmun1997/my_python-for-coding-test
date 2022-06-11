a, b = map(str, input().split())
max_len = max(len(a), len(b))
if len(a) < len(b):
    a = '0' * (max_len - len(a)) + a
else:
    b = '0' * (max_len - len(b)) + b

answer = ''
for i in range(max_len):
    answer += str(int(a[i]) + int(b[i]))

print(answer)