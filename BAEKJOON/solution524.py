n = int(input())
student = list(map(int, input().split()))

temp = [] # 임시 대기열
cookie = [] # 간식을 받은 학생
start = 1

# 3 2 1 4 5
while len(student) != 0:
    if start != student[0]:
        if temp and start == temp[-1]:
            cookie.append(temp.pop())
            start += 1
        else:
            temp.append(student.pop(0))
    else:
        cookie.append(student.pop(0))
        start += 1

while temp:
    cookie.append(temp.pop())

sorted_cookie = sorted(cookie)
if sorted_cookie == cookie:
    print("Nice")
else:
    print("Sad")