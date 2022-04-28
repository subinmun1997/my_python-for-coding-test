def solution(n):
    array = ''
    while n:
        array += str(n%3)
        n //= 3
    array = int(array, 3)
    return array

print(solution(45))
print(solution(125))