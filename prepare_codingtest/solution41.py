n = int(input())
students = []

for _ in range(n):
    x = input().split()
    students.append((x[0], int(x[1])))

students = sorted(students, key=lambda l : l[1])

for i in students:
    print(i[0], end=' ')