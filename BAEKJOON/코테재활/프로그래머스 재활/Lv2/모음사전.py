from itertools import product

def solution(word):
    aeiou = ['A','E','I','O','U']
    answer = set()
    for i in range(1, len(aeiou)+1):
        permut = product(aeiou, repeat=i)
        for c in permut:
            answer.add(''.join(c))

    answer = sorted(answer)
    return answer.index(word)+1

print(solution("AAAAE"))
print(solution("AAAE"))
print(solution("I"))
print(solution("EIO"))