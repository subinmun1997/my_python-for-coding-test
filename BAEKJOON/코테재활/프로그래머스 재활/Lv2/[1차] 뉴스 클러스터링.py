from collections import Counter

def solution(str1, str2):
    # 소문자로 변경
    str1, str2 = str1.lower(), str2.lower()

    # 문자열 조각들 만들기
    str1_set = list(str1[i:i+2] for i in range(len(str1)-1) if str1[i:i+2].isalpha())
    str2_set = list(str2[i:i+2] for i in range(len(str2)-1) if str2[i:i+2].isalpha())

    # 문자열 조각들 세기
    str1_counter, str2_counter = Counter(str1_set), Counter(str2_set)

    len_inter = sum((str1_counter & str2_counter).values()) # 교집합 개수
    len_union = sum((str1_counter | str2_counter).values()) # 합집합 개수

    return 65536 if len_union == 0 and len_inter == 0 else int(len_inter / len_union * 65536)

print(solution("FRANCE", "french"))
print(solution("handshake", "shake hands"))
print(solution("aa1+aa2", "AAAA12"))
print(solution("E=M*C^2", "e=m*c^2"))
