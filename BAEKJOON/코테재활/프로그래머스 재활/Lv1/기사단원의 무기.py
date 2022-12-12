def divisor(n):
    stack = []
    for i in range(1, int(n**0.5)+1):
        if n%i == 0:
            stack.append(n//i)
            stack.append(i)
    return len(set(stack))

def solution(number, limit, power):
    return sum([divisor(i) if divisor(i) <= limit else power for i in range(1, number+1)])

print(solution(5,3,2))
print(solution(10,3,2))
