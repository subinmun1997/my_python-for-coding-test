t = int(input())

for _ in range(t):
    n = int(input())
    course, score = [], []
    for _ in range(n):
        x, y = map(float, input().split())
        course.append(int(x))
        score.append(x * y)
    print(sum(course), end=' ')
    print("{:.1f}".format(sum(score)/sum(course)))

