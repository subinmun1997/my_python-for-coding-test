n = int(input())
card = list(map(int, input().split()))
m = int(input())
check = list(map(int, input().split()))

card_dict = {}
for i in card:
    if i not in card_dict:
        card_dict[i] = 1
    else:
        card_dict[i] += 1

for i in check:
    if i in card_dict.keys():
        print(card_dict[i], end=' ')
    else:
        print(0, end=' ')