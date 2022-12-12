def solution(babbling):
    answer = 0
    for b in babbling:
        for w in ["aya", "ye", "woo", "ma"]:
            if w * 2 not in b:
                b = b.replace(w, ' ') # "myea" 이런 경우 때문에 '' 대신  ' '
        if len(b.strip()) == 0:
            answer += 1
    return answer

print(solution(["aya", "yee", "u", "maa"]))
print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))