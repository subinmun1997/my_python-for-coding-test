n = int(input())
n_six = 666
answer = 0

while True:
    if '666' in str(n_six):
        answer += 1
    if answer == n:
        print(n_six)
        break
    n_six += 1

