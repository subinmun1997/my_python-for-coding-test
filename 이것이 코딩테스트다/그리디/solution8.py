s = input()

answer = 0
for i in s:
    if int(i) <= 1 or answer <= 1: # 두 수 중에서 하나라도 1 이하라면 더하는게 이득
        answer += int(i)
    else:
        answer *= int(i)

print(answer)