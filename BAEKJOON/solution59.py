n = int(input())

result = []
def solution(n):
    if n < 100:
        for i in range(1,n+1):
            result.append(i)
    elif n <= 1000:
        for i in range(1,100):
            result.append(i)
        for i in range(100,n+1):
            a = (i//100) - ((i%100)//10)
            b = ((i%100)//10) - ((i%100)%10)
            if a == b:
                result.append(i)
    print(len(result))

solution(n)

