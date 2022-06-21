def solution(answers):
    pattern1 = [1,2,3,4,5]
    pattern2 = [2,1,2,3,2,4,2,5]
    pattern3 = [3,3,1,1,2,2,4,4,5,5]
    score = [0,0,0]
    answer = []

    for idx, s in enumerate(answers):
        if s == pattern1[idx%len(pattern1)]:
            score[0] += 1
        if s == pattern2[idx%len(pattern2)]:
            score[1] += 1
        if s == pattern3[idx%len(pattern3)]:
            score[2] += 1

    for idx, s in enumerate(score):
        if s == max(score):
            answer.append(idx+1)

    return answer

print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))