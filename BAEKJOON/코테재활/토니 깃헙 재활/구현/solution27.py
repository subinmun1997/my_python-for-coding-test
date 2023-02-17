n = int(input())
# 학생, 학생이 좋아하는 다른 학생 리스트
students = [list(map(int, input().split())) for _ in range(n**2)]
# 학생들의 최종 자리
pos = [[0] * n for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for s in range(n**2):
    student = students[s]

    temp = [] # 해당 학생이 앉을 수 있는 모든 자리 담는 임시 배열
    for x in range(n):
        for y in range(n):
            if pos[x][y] == 0: # 해당 자리가 비어 있다면
                like = 0 # 좋아하는 친구 수
                blank = 0 # 비어있는 자리 수
                for k in range(4): # 상 하 좌 우 돌면서 문제 조건 파악
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0 <= nx < n and 0 <= ny < n: # 범위를 만족하고
                        if pos[nx][ny] in student[1:]: # 해당 학생의 좋아하는 친구 리스트에 포함된다면
                            like += 1
                        if pos[nx][ny] == 0: # 비어있는 자리라면
                            blank += 1

                temp.append((like, blank, x, y))

    # 정렬 기준 1.좋아하는 친구가 많을수록 2.빈 자리가 많을수록 3.행 번호가 작은 것부터 4.열 번호가 작은 것부터
    temp.sort(key=lambda x:(-x[0], -x[1], x[2], x[3]))
    pos[temp[0][2]][temp[0][3]] = student[0]

result = 0
students.sort() # 학생 순서대로 구하기 위해 정렬
for x in range(n):
    for y in range(n):
        cnt = 0
        for k in range(4): # 상 하 좌 우 회전하면서
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < n and 0 <= ny < n: # 범위를 만족하고
                if pos[nx][ny] in students[pos[x][y]-1]: # 학생이 좋아하는 다른 학생이라면
                    cnt += 1

        if cnt != 0:
            result += 10 ** (cnt-1) # 만족도 구하기

print(result)