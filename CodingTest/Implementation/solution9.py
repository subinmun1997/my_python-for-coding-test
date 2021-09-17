'''
문제 : 문자열 압축

문제 해설 :  입력으로 주어지는 문자열의 길이가 1,000 이하이기 때문에 가능한 모든 경우의 수를 탐색하는 완전 탐색을 수행할 수 있다.
             예를 들어, 길이가 N인 문자열이 입력되었다면 1부터 N/2까지의 모든 수를 단위로 하여 문자열을 압축하는 방법을 모두 확인하고
             가장 짧게 압축되는 길이를 출력하면 된다.
'''

def solution(s):
    answer = len(s)
    for step in range(1, len(s)//2+1): # 1개 단위(step)부터 압축 단위를 늘려가며 확인
        compressed = ""
        prev = s[0:step] # 앞에서부터 step만큼의 문자열 추출
        count = 1
        for j in range(step,len(s),step): # 단위(step) 크기만큼 증가시키며 이전 문자열과 비교
            if prev == s[j:j+step]:
                count += 1
            else: # 다른 문자열이 나왔다면(더 이상 압축하지 못하는 경우라면)
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j+step]
                count = 1
        compressed += str(count) + prev if count >= 2 else prev # 남아 있는 문자열에 대해서 처리
        answer = min(answer, len(compressed)) # 만들어지는 압축 문자열이 가장 짧은 것이 정답
    return answer

print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))