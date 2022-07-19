n = int(input())

def check(word):
    temp = []
    flag = True
    for i in range(len(word)-1):
        if word[i] != word[i+1]:
            if word[i] not in temp:
                temp.append(word[i])
            else:
                flag = False

    return flag

count = 0
for _ in range(n):
    word = input()
    word += '0'
    if check(word):
        count += 1

print(count)