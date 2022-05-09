def solution(numbers, hand):
    answer = ''
    left = [1,4,7]
    right = [3,6,9]

    s_left = [3,0]
    s_right = [3,2]
    pos = [[3,1],[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
    for i in numbers:
        if i in left:
            answer += 'L'
            s_left = pos[i]
        elif i in right:
            answer += 'R'
            s_right = pos[i]
        else:
            target = pos[i]
            diff_left = abs(target[0]-s_left[0]) + abs(target[1]-s_left[1])
            diff_right = abs(target[0] - s_right[0]) + abs(target[1] - s_right[1])
            if diff_right > diff_left:
                answer += 'L'
                s_left = pos[i]
            elif diff_right < diff_left:
                answer += 'R'
                s_right = pos[i]
            else:
                if hand == "right":
                    answer += 'R'
                    s_right = pos[i]
                else:
                    answer += 'L'
                    s_left = pos[i]
    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))