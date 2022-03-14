consonant = [["q","w","e","r","t"],["a","s","d","f","g"],["z","x","c","v"]]
vowel = [["y","u","i","o","p"],["h","j","k","l"],["b","n","m"]]

left, right = list(map(str, input().split()))
word = list(input())

for i in range(3):
    if left in consonant[i]:
        left = (i, consonant[i].index(left))
    if right in vowel[i]:
        right = (i, vowel[i].index(right) + len(consonant[i]))


answer = 0
for w in word:
    for i in range(3):
        if w in consonant[i]:
            temp_left = (i, consonant[i].index(w))
            answer += (abs(temp_left[0]-left[0]) + abs(temp_left[1]-left[1]))
            left = temp_left

        elif w in vowel[i]:
            temp_right = (i, vowel[i].index(w) + len(consonant[i]))
            answer += (abs(temp_right[0]-right[0]) + abs(temp_right[1]-right[1]))
            right = temp_right

print(answer + len(word))