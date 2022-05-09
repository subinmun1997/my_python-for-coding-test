def solution(a, b):
    return sum(a*b for a, b in zip(a, b))

print(solution([1,2,3,4],[-3,-1,0,2]))
print(solution([-1,0,1],[1,0,-1]))