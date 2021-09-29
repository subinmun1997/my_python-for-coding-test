c = int(input())

data = [list(map(int, input().split())) for _ in range(c)]

for i in data:
    student = i[0]
    score = i[1:]
    avg = sum(score)/student
    good = [i for i in score if i > avg]

    print("{:.3f}".format(len(good)/student*100) + "%")
