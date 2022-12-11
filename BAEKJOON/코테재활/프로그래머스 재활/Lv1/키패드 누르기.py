def solution(numbers, hand):
    result = ''

    pos = [[3,1],[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
    left = [1,4,7]
    right = [3,6,9]

    cur_left = [3,0]
    cur_right = [3,2]

    for num in numbers:
        if num in left:
            result += 'L'
            cur_left = pos[num]
        elif num in right:
            result += 'R'
            cur_right = pos[num]
        else:
            diff_left = abs(cur_left[0] - pos[num][0]) + abs(cur_left[1] - pos[num][1])
            diff_right = abs(cur_right[0] - pos[num][0]) + abs(cur_right[1] - pos[num][1])
            if diff_left < diff_right:
                result += 'L'
                cur_left = pos[num]
            elif diff_left > diff_right:
                result += 'R'
                cur_right = pos[num]
            else:
                if hand == 'left':
                    result += 'L'
                    cur_left = pos[num]
                else:
                    result += 'R'
                    cur_right = pos[num]

    return result

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))