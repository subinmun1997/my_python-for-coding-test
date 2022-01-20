piece = [1,1,2,2,2,8]

has_piece = list(map(int, input().split()))

for i in range(len(piece)):
    print(piece[i]-has_piece[i], end=' ')