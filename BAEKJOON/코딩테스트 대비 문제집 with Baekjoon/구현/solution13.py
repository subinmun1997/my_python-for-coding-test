consonant = [['q','w','e','r','t'], ['a','s','d','f','g'], ['z','x','c','v']]
vowels = [['y','u','i','o','p'], ['h','j','k','l'], ['b','n','m']]

left, right = map(str, input().split())
word = input()

for i in range(3):
    if left in consonant[i]:
        left = (i, consonant[i].index(left))
    if right in vowels[i]:
        right = (i, vowels[i].index(right) + len(consonant[i]))

result = 0
for w in word:
    for i in range(3):
        if w in consonant[i]:
            temp_left = (i, consonant[i].index(w))
            result += (abs(temp_left[0]-left[0]) + abs(temp_left[1]-left[1]))
            left = temp_left
        elif w in vowels[i]:
            temp_right = (i, vowels[i].index(w) + len(consonant[i]))
            result += (abs(temp_right[0]-right[0]) + abs(temp_right[1]-right[1]))
            right = temp_right

print(result + len(word))