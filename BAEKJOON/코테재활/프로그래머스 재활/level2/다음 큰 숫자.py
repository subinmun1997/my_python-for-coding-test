def same(num, target):
    temp = bin(num)[2:].count('1')
    return target == temp

def solution(n):
    numone = bin(n)[2:].count('1')
    for i in range(n+1, 1000001):
        if same(i, numone):
            return i

print(solution(78))
print(solution(15))
