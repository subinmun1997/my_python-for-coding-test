n, m, k = map(int, input().split())
numbers = sorted(list(map(int, input().split())), reverse=True)

first = numbers[0]
second = numbers[1]

count = int(m/(k+1))*k
count += m%(k+1)

answer = 0
answer += count * first
answer += (m-count) * second

print(answer)
