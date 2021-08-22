n = int(input())

students = []
for i in range(n):
    input_data = input().split()
    students.append((input_data[0], int(input_data[1])))

students = sorted(students, key=lambda student:students[1])

for i in students:
    print(i[0], end=' ')