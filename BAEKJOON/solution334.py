n = int(input())

students = []
for _ in range(n):
    names, d, m, y = map(str, input().split())
    students.append((names, int(d), int(m), int(y)))
    students.sort(key=lambda x:(x[3],x[2],x[1]))

if n == 1:
    print(students[0][0])
else:
    print(students[n-1][0])
    print(students[0][0])