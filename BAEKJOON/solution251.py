n, m = map(int, input().split()) # 끊어진 기타줄 개수, 기타줄 브랜드

g = []
answer = 0
for _ in range(m):
    p, s = map(int, input().split()) # 패키지, 낱개
    g.append((p,s))

six_list = sorted(g, key=lambda x : x[0])
one_list = sorted(g, key=lambda x : x[1])

if six_list[0][0] <= one_list[0][1] * 6:
    answer += six_list[0][0] * (n//6)
    if six_list[0][0] < one_list[0][1] * (n%6):
        answer += six_list[0][0]
    else:
        answer += one_list[0][1] * (n%6)
else:
    answer = one_list[0][1] * n

print(answer)