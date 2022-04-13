students = [int(input()) for _ in range(28)]
students.sort()

for i in range(1, 31):
    if i not in students:
        print(i)