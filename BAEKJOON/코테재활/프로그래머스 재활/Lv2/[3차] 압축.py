def solution(msg):
    msg += '0'
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    dictionary = {k:v for (k,v) in zip(alphabet, list(range(1,27)))}
    answer = []

    word = ''
    next_num = 27
    for i in range(len(msg)-1):
        word += msg[i]
        if word + msg[i+1] in dictionary.keys():
            continue
        else:
            answer.append(dictionary[word])
            dictionary[word+msg[i+1]] = next_num
            word = ''
            next_num += 1

    return answer

print(solution("KAKAO"))
print(solution("TOBEORNOTTOBEORTOBEORNOT"))
print(solution("ABABABABABABABAB"))

