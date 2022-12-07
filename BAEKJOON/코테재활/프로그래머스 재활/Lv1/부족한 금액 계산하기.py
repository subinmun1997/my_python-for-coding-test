def solution(price, money, count):
    cost = sum(price * i for i in range(1, count+1))
    return cost - money if cost > money else 0

print(solution(3, 20, 4))