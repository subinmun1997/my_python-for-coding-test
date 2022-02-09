piece = list(map(int, input().split()))
sorted_piece = sorted(piece)

while True:
    if piece == sorted_piece:
        break
    else:
        for i in range(len(piece)-1):
            if piece[i] > piece[i+1]:
                piece[i], piece[i+1] = piece[i+1], piece[i]
                for p in piece:
                    print(p, end=' ')
                print()
