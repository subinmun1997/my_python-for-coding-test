n = int(input())

count = 0
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                count += 1

print(count)

'''
이러한 유형은 완전 탐색 유형으로 분류되기도 한다. 완전 탐색 알고리즘은 가능한 경우의 수를
모두 검사해보는 탐색 방법이다.
'''