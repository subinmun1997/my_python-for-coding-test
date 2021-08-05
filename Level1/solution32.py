def solution(seoul):
    answer = ''
    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            return "김서방은 {}에 있다".format(i)

print(solution(["Jane","Kim"]))

# 한 줄 코드

# def solution(seoul):
#   return "김서방은 {}에 있다".format(seoul.index('Kim'))
