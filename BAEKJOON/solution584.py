n = int(input())
pan = []

for _ in range(n):
    pan.append(list(map(int, input().split())))

first = sorted(pan, key=lambda x : x[0], reverse=True)
last = sorted(pan, key=lambda x : x[1])

last_start = first[0][0]
first_end = last[0][1]

# 제일 늦게 시작하는 start에서 제일 일찍 끝나는 end를 빼주면 정답
result = last_start - first_end
if result <= 0:
    print(0)
else:
    print(result)
