n = int(input())
number = list(map(int, input().split()))

student = []
for i in range(n):
    student.insert(i-number[i],i+1)

print(*student)