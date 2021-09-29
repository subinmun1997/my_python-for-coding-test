c = int(input())

data = [list(map(int, input().split())) for _ in range(c)]
print(data)
for i in data:
    student = i[0]
    print(student)
    score = i[1:]
    print(score)
    avg = sum(score)/student
    print(avg)
    good = [i for i in score if i > avg]

    print("{:.3f}".format(len(good)/student*100) + "%")
