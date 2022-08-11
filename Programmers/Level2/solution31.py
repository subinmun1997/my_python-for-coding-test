import math

def solution(arr):
    while len(arr) != 1:
        a = arr.pop()
        b = arr.pop()
        arr.append(a*b // math.gcd(a, b))
    return arr[0]

print(solution([2,6,8,14]))
print(solution([1,2,3]))
