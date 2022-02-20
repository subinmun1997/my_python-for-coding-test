n = int(input())

students = []
for i in range(1, n+1):
    scores = list(map(int, input().split()))
    students.append(scores)
students.sort(key=lambda x : x[0])

for i in range(1, 5):
    winner = max(students, key=lambda x: (x[i],-x[0]))

    students[winner[0]-1] = [-1,-1,-1,-1,-1]
    print(winner[0], end=' ')