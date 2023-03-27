'''
아이디어: 거꾸로 2로 나눠가면서 구하자. 2로 안나눠지면 점프가 필요한거니까 건전지 사용 + 1

좀 더 생각해보면, 2의 n제곱이면 처음 0 -> 1 빼고 순간이동으로 갈 수 있다. 이를 이진수로 표현해보면
1이 하나인 이진수이다. 즉, 건전지 사용량은 이진수로 변환했을 때 1의 개수와 같다.
'''
def solution(n):
    count = 0
    while n > 0:
        count += n % 2
        n //= 2
    return count

# def solution(n):
#     return bin(n).count('1')

print(solution(5))
print(solution(6))
print(solution(5000))