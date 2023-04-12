def is_prime(n):
    # 1은 소수가 아님
    if n <= 1:
        return False
    # n의 제곱근까지 살펴보면서
    for i in range(2, int(n**0.5)+1):
        # 나뉘는 수가 있다면 소수가 아님
        if n % i == 0:
            return False
    return True

def is_palindrome(n):
    # 팰린드롬이라면 true
    return str(n) == str(n)[::-1]

# 입력으로 주어진 수
n = int(input())

while True:
    # n보다 크거나 같은 수 중에서, 소수이면서 팰린드롬인 수가 있다면 출력하고 종료
    if is_palindrome(n) and is_prime(n):
        print(n)
        break
    n += 1