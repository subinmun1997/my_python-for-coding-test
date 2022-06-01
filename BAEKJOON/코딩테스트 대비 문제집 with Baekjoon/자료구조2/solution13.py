t = int(input())
for _ in range(t):
    n = int(input())
    clothes = {}
    for _ in range(n):
        kind, body = map(str, input().split())
        if body in clothes:
            clothes[body] += 1
        else:
            clothes[body] = 1

    values = list(clothes.values())
    answer = 1
    '''
    여기서 종류수에 +1을 해준 이유는 그 종류의 의상을 착용해도 되고 안해도 되기 때문이고
    마지막에 -1을 해준 이유는 모든 의상을 착용하지 않은 경우를 제외시켜줘야 하기 때문이다.
    '''
    for value in values:
        answer *= (value+1)
    print(answer-1)