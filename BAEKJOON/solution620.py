t = int(input())

for _ in range(t):
    m, kind = list(map(str, input().split())) # 개수, 문제의 종류
    if kind == 'C': # 알파벳 -> 숫자
        exam = list(map(str, input().split()))
        for e in exam:
            print(int(ord(e)) - int(ord('A')) + 1, end=' ')
        print()
    else: # 숫자 -> 알파벳
        exam = list(map(int, input().split()))
        for e in exam:
            print(chr(65 + e - 1), end=' ')
        print()
