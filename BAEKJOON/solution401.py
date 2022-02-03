t = int(input())

for _ in range(t):
    n = int(input())
    player1 = player2 = 0
    for _ in range(n):
        p1, p2 = input().split()

        if p1 == p2:
            continue
        elif (p1 == 'R' and p2 == 'P') or (p1 == 'P' and p2 == 'S') or (p1 == 'S' and p2 == 'R'):
            player2 += 1
        else:
            player1 += 1

    if player1 > player2:
        print("Player1")
    elif player1 < player2:
        print("Player2")
    else:
        print("TIE")