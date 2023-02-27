def check(word):
    vowel = 'aeiou'
    count_v = 0

    for i in range(len(word)):
        if word[i] in vowel:
            count_v += 1
        if i > 0:
            if word[i] == word[i-1] and word[i] != 'e' and word[i] != 'o': # 같은 글자 연속적이면X, 단 ee, oo 제외
                return False
        if i > 1:
            if word[i] not in vowel: # 자음 연속 3개X
                if word[i-1] not in vowel:
                    if word[i-2] not in vowel:
                        return False
            if word[i] in vowel: # 모음 연속 3개X
                if word[i-1] in vowel:
                    if word[i-2] in vowel:
                        return False
    if count_v < 1: # 모음 개수 1개 이상
        return False

    return True

while True:
    word = input()
    if word == "end":
        break
    if check(word):
        print("<" + word + ">", "is acceptable.")
    else:
        print("<" + word + ">", "is not acceptable.")