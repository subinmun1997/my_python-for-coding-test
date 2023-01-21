left_key = [['q', 'w', 'e', 'r', 't'], ['a', 's', 'd', 'f', 'g'], ['z', 'x', 'c', 'v']]
right_key = [['y', 'u', 'i', 'o', 'p'], ['h', 'j', 'k', 'l'], ['b', 'n', 'm']]

left_hand, right_hand = map(str, input().split())
word = input()

for i in range(3):
    if left_hand in left_key[i]:
        left_hand = (i, left_key[i].index(left_hand))
    if right_hand in right_key[i]:
        right_hand = (i, right_key[i].index(right_hand) + len(left_key[i]))

result = 0
for w in word:
    for i in range(3):
        if w in left_key[i]:
            temp_left = (i, left_key[i].index(w))
            result += (abs(left_hand[0] - temp_left[0]) + abs(left_hand[1] - temp_left[1]))
            left_hand = temp_left
        elif w in right_key[i]:
            temp_right = (i, right_key[i].index(w) + len(left_key[i]))
            result += (abs(right_hand[0] - temp_right[0]) + abs(right_hand[1] - temp_right[1]))
            right_hand = temp_right

print(result + len(word))