'''
문제 : 시각

문제 해설 : 이 문제는 모든 시각의 경우를 하나씩 모두 세서 쉽게 풀 수 있는 문제다. 왜냐하면 하루는 86.400초로
            모든 경우는 86,400가지밖에 존재하지 않기 때문이다.
            따라서 단순히 시각을 1씩 증가시키면서 3이 하나라도 포함되어 있는지 확인하면 될 것이다. 전체 시, 분, 초에
            대한 경우의 수는 24 x 60 x 60이며 3중 반복문을 이용해 계산할 수 있다.
'''

n = int(input())

total = 0
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            time = str(i) + str(j) + str(k)

            if '3' in time:
                total += 1

print(total)