from collections import Counter

w = input()
l = Counter(w) # Counter 함수는 문자열 속 문자 개수를 가장 많은 것부터 내림차순으로 딕셔너리 형태로 반환
odd = ''

for key, val in l.items():
    if val % 2 != 0:
        odd += key

if len(odd) > 1:
    print("I'm Sorry Hansoo")
else:
    d = sorted(l.items())
    for j in d:
        print(j[0]*(j[1]//2), end='')
    print(odd, end='')
    for j in d[::-1]:
        print(j[0]*(j[1]//2), end='')