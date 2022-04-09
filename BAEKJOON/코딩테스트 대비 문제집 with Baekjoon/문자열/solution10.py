vows = 'aeiou'

while True:
    s = input()
    if s == "end":
        break
    count_v = 0
    flag = True
    for i in range(len(s)):
        if s[i] in vows:
            count_v = 1
        if i > 0:
            if s[i] == s[i - 1] and s[i] != 'e' and s[i] != 'o':
                flag = False
                break
        if i > 1:
            if s[i] not in vows:
                if s[i - 1] not in vows:
                    if s[i - 2] not in vows:
                        flag = False
                        break
            if s[i] in vows:
                if s[i - 1] in vows:
                    if s[i - 2] in vows:
                        flag = False
                        break

    if count_v == 1 and flag:
        print("<" + s + "> is acceptable.")
    else:
        print("<" + s + "> is not acceptable.")