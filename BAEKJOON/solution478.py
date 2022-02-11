t = int(input())

for _ in range(t):
    n = int(input()) #방의 개수
    room = [True] * (n+1)

    for i in range(2, n+1):
        for j in range(i, n+1):
            if j%i == 0:
                if room[j] == True:
                    room[j] = False
                else:
                    room[j] = True

    print(room.count(True)-1)