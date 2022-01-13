n = int(input())
students = []

for _ in range(n):
    name, k, e, m = map(str, input().split())
    students.append((name, int(k), int(e), int(m)))

students = sorted(students, key=lambda x : (-x[1],x[2],-x[3],x[0]))

for i in students:
    print(i[0])