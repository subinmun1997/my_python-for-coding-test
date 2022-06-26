def solution(numbers, hand):
    left = [1,4,7]
    right = [3,6,9]

    s_left = [3,0]
    s_right = [3,2]
    pos = [[3,1], [0,0], [0,1], [0,2], [1,0], [1,1], [1,2], [2,0], [2,1], [2,2]]

    answer = ''
    for i in numbers:
        if i in left:
            answer += 'L'
            s_left = pos[i]
        elif i in right:
            answer += 'R'
            s_right = pos[i]
        else:
            move = pos[i]
            move_left = abs(s_left[0] - move[0]) + abs(s_left[1] - move[1])
            move_right = abs(s_right[0] - move[0]) + abs(s_right[1] - move[1])
            if move_left > move_right:
                answer += 'R'
                s_right = pos[i]
            elif move_right > move_left:
                answer += 'L'
                s_left = pos[i]
            else:
                if hand == 'left':
                    answer += 'L'
                    s_left = pos[i]
                else:
                    answer += 'R'
                    s_right = pos[i]

    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))