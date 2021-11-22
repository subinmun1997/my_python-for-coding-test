n, m, x, y, k = map(int, input().split())

array = []
for _ in range(n):
    array.append(list(map(int, input().split())))

action = list(map(int, input().split()))

dice = [0,0,0,0,0,0,0]
dx = [0,0,0,-1,1] # 동 서 북 남
dy = [0,1,-1,0,0]

now_x = x
now_y = y

while len(action) > 0:
    key = action.pop(0)
    nx = dx[key] + now_x
    ny = dy[key] + now_y

    if nx < 0 or ny < 0 or n <= nx or m <= ny:
        continue

    else:
        now_x = nx
        now_y = ny
        if key == 1:
            dice = [0, dice[3], dice[2], dice[6], dice[1], dice[5], dice[4]]

            if array[now_x][now_y] == 0:
                array[now_x][now_y] = dice[1]

            else:
                dice[1] = array[now_x][now_y]
                array[now_x][now_y] = 0

            print(dice[6])

        elif key == 2:
            dice = [0, dice[4], dice[2], dice[1], dice[6], dice[5], dice[3]]

            if array[now_x][now_y] == 0:
                array[now_x][now_y] = dice[1]

            else:
                dice[1] = array[now_x][now_y]
                array[now_x][now_y] = 0
            print(dice[6])

        elif key == 3:
            dice = [0, dice[2], dice[6], dice[3], dice[4], dice[1], dice[5]]

            if array[now_x][now_y] == 0:
                array[now_x][now_y] = dice[1]

            else:
                dice[1] = array[now_x][now_y]
                array[now_x][now_y] = 0
            print(dice[6])

        else:
            dice = [0, dice[5], dice[1], dice[3], dice[4], dice[6], dice[2]]

            if array[now_x][now_y] == 0:
                array[now_x][now_y] = dice[1]

            else:
                dice[1] = array[now_x][now_y]
                array[now_x][now_y] = 0
            print(dice[6])