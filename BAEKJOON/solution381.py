students = []

for _ in range(28):
    students.append(int(input()))

thirty = [i for i in range(1, 31)]
bad_students = []
for i in thirty:
    if i not in students:
        bad_students.append(i)

bad_students.sort()
for i in bad_students:
    print(i)