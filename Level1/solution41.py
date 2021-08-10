def solution(n):
    ls = list(str(n))
    ls.sort(reverse = True)
    return int("".join(ls))

print(solution(118372))