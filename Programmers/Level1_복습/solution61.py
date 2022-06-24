number = {'zero':"0", 'one':"1", 'two':"2", 'three':"3", 'four':"4", 'five':"5", 'six':"6", 'seven':"7", 'eight':"8", 'nine':"9"}

def solution(s):
    answer = s
    for key, value in number.items():
        answer = answer.replace(key, value)

    return answer


print(solution("one4seveneight"))
print(solution("23four5six7"))
print(solution("2three45sixseven"))
print(solution("123"))