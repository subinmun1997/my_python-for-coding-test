def solution(a,b):
    answer = ''
    day = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    dic = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    add = 0
    for i in range(1,a):
        add += dic[i]
    answer = add + b - 1
    answer = day[answer%7]
    return answer

print(solution(5,24))