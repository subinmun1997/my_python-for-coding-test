from itertools import permutations

def solution(numbers):
    temp = set()
    answer = 0
    for i in range(1, len(numbers)+1):
        permut = permutations(numbers, i)
        for pm in permut:
            temp.add(''.join(pm))

    temp = [int(i) for i in temp]
    for i in set(temp):
        if is_prime(i):
            answer += 1

    return answer

def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

print(solution("17"))
print(solution("011"))