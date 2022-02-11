n, t = map(int, input().split())

time = 0
count = 0
while True:
    fcfs = list(map(int, input().split()))
    for f in fcfs:
        if time+f <= t:
            time += f
            count += 1
        else:
            break
    break

print(count)