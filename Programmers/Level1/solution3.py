def solution(phone_numbers):
    return '*' * (len(phone_numbers) - 4) + phone_numbers[-4:]

print(solution("01033334444"))
print(solution("027778888"))