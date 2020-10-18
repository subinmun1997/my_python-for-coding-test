n,m = map(int,input().split())

d = [[0]*m for i in range(n)] #0이라는 값을 m번 반복하는 배열로 만든다
x,y,direction = map(int,input().split()) #현 위치, 방향 지정
d[x][y] = 1 #현재 위치 마킹

array = []
for i in range(n):
    array.append(list(map(int,input().split())))

dx = [-1,0,1,0] #x=행 y=열
dy = [0,1,0,-1] #북 동 남 서

def turn_left(): #왼쪽으로 회전
    global direction
    direction -= 1 #서->남(3->2) 남->동(2->1) 동->북(1->0) 왼쪽으로 회전시 -1씩 감소
    if direction == -1: #북->서 예외
        direction = 3 #서쪽방향(3) 지정

count = 1 #현재 위치도 마킹
turn_time = 0
while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    if d[nx][ny] == 0 and array[nx][ny] == 0: #아직 안 간 장소라면 && 육지라면
        d[nx][ny] = 1
        x = nx
        y = ny
        count+=1 #이동했으니까
        turn_time = 0
        continue
    else: #방문했거나 바다라면
        turn_time += 1
    if turn_time == 4: #동서남북이 바다라면
        nx = x - dx[direction] #뒤로 이동
        ny = y - dy[direction]

        if array[nx][ny] == 0: #뒤로 이동할 때 육지라서 이동 가능하다면
            x = nx
            y = ny
        else: #이동 불가능 하다면 break
            break
        turn_time = 0

print(count)