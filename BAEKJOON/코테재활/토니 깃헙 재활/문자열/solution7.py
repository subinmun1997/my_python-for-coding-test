def check(word):
    temp = []
    for i in range(len(word)-1):
        if word[i] != word[i+1]:
            if word[i] not in temp:
                temp.append(word[i])
            else:
                return False
    return True

n = int(input())

count = 0
for _ in range(n):
    word = input() + '0'
    if check(word):
        count += 1

print(count)
