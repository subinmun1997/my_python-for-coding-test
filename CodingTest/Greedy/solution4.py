'''
이 문제는 M이 10,000 이하이므로 solution2의 방법으로도 해결할 수 있지만 M의 크기가 100억 이상처럼 커진다면 시간 초과 판정을
받을 것이다. 반복되는 수열 방법으로 풀이.

이 문제는 가장 큰 수와 두 번째로 큰 수가 더해질 때는 특정한 수열 형태로 일정하게 반복해서 더해지는 특징이 있다.
반복되는 수열의 길이는 (k+1)
따라서 m을 (k+1)로 나는 몫이 수열이 반복되는 횟수가 된다. 다시 여기에 k를 곱해주면 가장 큰 수가 등장하는 횟수가 된다.

m이 (k+1)로 나누어떨어지지 않는 경우는 m을 (k+1)로 나눈 나머지만큼 가장 큰 수가 추가로 더해지므로
가장 큰 수가 더해지는 횟수는 int(m/(k+1)) * k + m%(k+1)과 같다.
'''
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

count = (m//(k+1))*k
count += m%(k+1)

result = 0
result += first * count
result += second * (m-count)

print(result)