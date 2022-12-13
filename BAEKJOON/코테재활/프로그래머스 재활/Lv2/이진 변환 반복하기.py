def solution(s):
    bin_count = 0
    remove_zero = 0
    while s != '1':
        remove_zero += s.count('0')
        s = s.replace('0', '')
        s = bin(len(s))[2:]
        bin_count += 1
    return [bin_count, remove_zero]

print(solution("110010101001"))
print(solution("01110"))
print(solution("1111111"))