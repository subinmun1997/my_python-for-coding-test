s = input()
answer = 0

for i in map(int, s):
    if answer <= 1 or i <= 1:
        answer += i
    else:
        answer *= i

print(answer)