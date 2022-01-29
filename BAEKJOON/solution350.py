cards = [i for i in range(1, 21)]

for _ in range(10):
    a, b = map(int, input().split())
    temp = cards[a-1:b]
    temp = reversed(temp)
    cards[a-1:b] = temp

for i in range(len(cards)):
    print(cards[i], end=' ')