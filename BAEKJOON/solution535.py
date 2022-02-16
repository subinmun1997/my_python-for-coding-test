n = int(input())

questions = []
for _ in range(n):
    questions.append(input().split())

questions.sort(key=lambda x : x[1])
print(questions[0][0])