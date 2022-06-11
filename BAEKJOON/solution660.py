w = input()
answer = ''
vowel = 'aeiou'

cur = 0
while cur < len(w):
    answer += w[cur]
    if w[cur] in vowel:
        cur += 3
    else:
        cur += 1

print(answer)