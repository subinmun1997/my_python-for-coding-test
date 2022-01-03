# 문제 해결 아이디어 : 모든 5를 6으로 착각했을 때가 최댓값, 모든 6를 5로 착각했을 때가 최솟값이다.

n1,n2 = input().split()

minX = int(n1.replace('6','5')) + int(n2.replace('6','5'))
maxX = int(n1.replace('5','6')) + int(n2.replace('5','6'))

print(minX, maxX)