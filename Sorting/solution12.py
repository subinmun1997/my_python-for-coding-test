n = int(input())

students = []
for i in range(n):
    input_data = input().split()
    students.append((input_data[0], int(input_data[1])))

def setting(data):
    return data[1]

students = sorted(students, key=setting)

for i in students:
    print(i[0], end=' ')