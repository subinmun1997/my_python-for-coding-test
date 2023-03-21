def solution(price, money, count):
    total = sum([price * i for i in range(1, count+1)])
    return max(0, total-money)

print(solution(3, 20, 4))