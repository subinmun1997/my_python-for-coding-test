import sys
input = sys.stdin.readline

n = int(input())
temp = list(map(int, input().split()))
m = int(input())
check = list(map(int, input().split()))

cards = {}
for i in temp:
    if i not in cards:
        cards[i] = 1
    else:
        cards[i] += 1

for i in check:
    if i in cards.keys():
        print(cards[i], end=' ')
    else:
        print(0, end=' ')

