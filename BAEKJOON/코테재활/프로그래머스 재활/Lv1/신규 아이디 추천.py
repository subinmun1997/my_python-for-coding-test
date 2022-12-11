def solution(new_id):
    result = ''
    option = ['-', '_', '.']
    # 1단계
    new_id = new_id.lower()
    # 2단계
    for id in new_id:
        if id.isalnum() or id in option:
            result += id
    # 3단계
    while '..' in result:
        result = result.replace('..', '.')
    # 4단계
    if result and result[0] == '.':
        if len(result) > 1:
            result = result[1:]
        else:
            result = ''
    if result and result[-1] == '.':
        if len(result) > 1:
            result = result[:-1]
        else:
            result = ''
    # 5단계
    if len(result) == 0:
        result += 'a'
    # 6단계
    if len(result) >= 16:
        result = result[:15]
        if result[-1] == '.':
            result = result[:-1]
    # 7단계
    if len(result) <= 2:
        while len(result) != 3:
            result += result[-1]

    return result

print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))