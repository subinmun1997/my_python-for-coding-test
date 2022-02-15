n = int(input())
card = [i for i in range(1, n+1)]
discard = []
while len(card) != 1:
    discard.append(card.pop(0))
    card.append(card.pop(0))

for d in discard:
    print(d, end=' ')
print(card[0])