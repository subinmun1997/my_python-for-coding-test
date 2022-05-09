def solution(s):
    answer = ''
    check = ''
    table = {"zero": 0,
             "one": 1,
             "two": 2,
             "three": 3,
             "four": 4,
             "five": 5,
             "six": 6,
             "seven": 7,
             "eight": 8,
             "nine": 9}
    if s.isdigit():
        return int(s)
    for i in range(len(s)):
        if s[i].isdigit():
            answer += s[i]
        else:
            check += s[i]
            if check in table:
                answer += str(table[check])
                check = ''

    return int(answer)

print(solution("one4seveneight"))
print(solution("23four5six7"))
print(solution("2three45sixseven"	))
print(solution("123"))