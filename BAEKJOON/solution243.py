n = int(input())
n_six = 666
count = 0

while True:
    if '666' in str(n_six): # n번째 수에 '666'이 포함되어 있다면
        count += 1 # 카운트를 올려라
    if count == n: # 카운트랑 n번째 수가 같다면
        print(n_six) # n_six를 출력하고
        break # while문을 종료해라
    n_six += 1 # 666이 포함된 수가 나올 때 까지 1씩 증가
