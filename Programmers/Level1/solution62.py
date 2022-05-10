def solution(new_id):
    possible = ["-", "_", "."]
    new_id = new_id.lower()

    temp = ''
    for i in new_id:
        if i.isalnum():
            temp += i
        if i in possible:
            temp += i
    new_id = temp

    while '..' in new_id:
        new_id = new_id.replace("..", ".")

    if len(new_id) >= 1:
        if new_id[0] == '.':
            new_id = new_id[1:]
    if len(new_id) >= 1:
        if new_id[-1] == '.':
            new_id = new_id[:-1]

    if len(new_id) == 0:
        new_id += 'a'

    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]

    if len(new_id) <= 2:
        while len(new_id) != 3:
            new_id += new_id[-1]

    return new_id

print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))