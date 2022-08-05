n = int(input())

score = []
for _ in range(n):
    name, kor, eng, math = map(str, input().split())
    score.append((name, int(kor), int(eng), int(math)))

score.sort(key=lambda x:(-x[1], x[2], -x[3], x[0]))
for i in score:
    print(i[0])