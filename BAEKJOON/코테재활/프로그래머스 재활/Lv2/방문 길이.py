def solution(dirs):
    x, y = 0, 0
    done = set()
    dx = [0, 0, 1, -1] # U D R L
    dy = [1, -1, 0, 0]
    make_load = ['U', 'D', 'R', 'L']

    for dir in dirs:
        for i in range(len(make_load)):
            if dir == make_load[i]:
                nx = x + dx[i]
                ny = y + dy[i]

        if nx > 5 or nx < -5 or ny > 5 or ny < -5:
            continue

        done.add((x, y, nx, ny)) # (x, y) -> (nx, ny) 인 경우와
        done.add((nx, ny, x, y)) # (nx, ny) -> (x, y) 인 경우는 같은 경로임
        x = nx
        y = ny

    return len(done) // 2


print(solution("ULURRDLLU"))
print(solution("LULLLLLLU"))