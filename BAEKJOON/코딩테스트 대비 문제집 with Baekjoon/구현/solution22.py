n = int(input())
count = 0

for _ in range(n):
    word = input()
    word += '1'
    temp = []
    flag = True
    for i in range(len(word)-1):
        if word[i] != word[i+1]:
            if word[i] not in temp:
                temp.append(word[i])
            else:
                flag = False
        else:
            continue
    if flag:
        count += 1

print(count)
