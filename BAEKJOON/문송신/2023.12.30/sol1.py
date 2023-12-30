t = int(input())

for _ in range(t):
    value, unit = input().split()
    value = float(value)

    answer_v = 0 # 정답 값
    answer_u = '' # 정답 단위

    if unit == 'kg':
        answer_u = 'lb'
        answer_v = value * 2.2046
    elif unit == 'lb':
        answer_u = 'kg'
        answer_v = value * 0.4536
    elif unit == 'l':
        answer_u = 'g'
        answer_v = value * 0.2642
    else:
        answer_u = 'l'
        answer_v = value * 3.7854

    # 정답 출력
    print(f"{answer_v:.4f}", answer_u)