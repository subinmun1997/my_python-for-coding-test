def solution(t, p):
    plen = len(p)
    count = 0
    for i in range(len(t)-plen+1):
        if int(t[i:i+plen]) <= int(p):
            count += 1
    return count

print(solution("3141592", "271"))
print(solution("500220839878", "7"))
print(solution("10203", "15"))