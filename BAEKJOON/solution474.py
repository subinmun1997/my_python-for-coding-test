answer = int(input())
while True:
    op = input()
    if op == '=':
        break
    n = int(input())
    if op == '+':
        answer += n
    elif op == '-':
        answer -= n
    elif op == '*':
        answer *= n
    elif op == '/':
        answer //= n
print(answer)