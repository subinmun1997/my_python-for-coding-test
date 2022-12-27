def solution(n, k):
    prime = change_prime(n, k).split('0')
    count = 0
    for i in prime:
        if i != '' and '0' not in i and check_prime(int(i)):
            count += 1
    return count

def change_prime(n, k):
    result = ''
    while n:
        result += str(n%k)
        n //= k
    return result[::-1]

def check_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

print(solution(437674, 3))
print(solution(110011, 10))