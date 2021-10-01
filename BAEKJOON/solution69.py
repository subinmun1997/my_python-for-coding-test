def solution(k,n):
    if k == 0:
        return n
    else:
        people = 0
        for i in range(1,n+1):
            people += solution(k-1,i)
        return people


t = int(input())

home = []
for _ in range(t):
    k = int(input())
    n = int(input())
    home.append(solution(k,n))

for i in home:
    print(i)