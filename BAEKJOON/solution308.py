n = int(input())

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

value = factorial(n)
value = list(str(value))
value.reverse()

cnt = 0
for v in value:
    if v == '0':
        cnt += 1
    else:
        break

print(cnt)