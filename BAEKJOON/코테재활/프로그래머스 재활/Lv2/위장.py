def solution(clothes):
    clo_dict = {}
    result = 1

    for x, y in clothes:
        if y in clo_dict:
            clo_dict[y] += 1
        else:
            clo_dict[y] = 1

    for i in clo_dict.values():
        result *= (i+1)

    return result - 1

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))