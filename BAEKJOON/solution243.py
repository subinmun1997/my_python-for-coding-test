n = int(input())
n_six = 666
count = 0

while True:
    if '666' in str(n_six):
        count += 1
    if count == n:
        print(n_six)
        break
    n_six += 1
