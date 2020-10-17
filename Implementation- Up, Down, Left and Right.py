n = int(input())
x,y = 1,1
plans = input().split() #이동방향 입력

dx = [0,0,-1,1] #서 동 북 남
dy = [-1,1,0,0]
move_types=['L','R','U','D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx<1 or ny<1 or nx>n or ny>n: # 공간을 벗어나는 경우 무시
        continue
    x,y = nx,ny

print(x,y)

