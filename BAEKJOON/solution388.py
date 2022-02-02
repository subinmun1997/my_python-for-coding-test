temp = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

n, b = map(int, input().split())
answer = ''

while n != 0:
    answer += str(temp[n%b])
    n = n//b

print(answer[::-1])