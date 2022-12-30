def solution(want, number, discount):
    answer = 0
    for day in range(len(discount) - 9):
        discountList = discount[day:day+10]
        for w, n in zip(want, number):
            if n == discountList.count(w):
                continue
            else:
                break
        else:
            answer += 1
    return answer

print(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))
print(solution(["apple"], [10], ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]))