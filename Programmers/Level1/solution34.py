def solution(sizes):
    max_value = []
    min_value = []

    for x, y in sizes:
        max_value.append(max(x, y))
        min_value.append(min(x, y))

    return max(max_value) * max(min_value)

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))