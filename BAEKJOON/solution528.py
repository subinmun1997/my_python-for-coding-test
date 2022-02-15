n, m = map(int, input().split())
location = list(map(int, input().split()))

queue = [i for i in range(1, n+1)]
count = 0

for i in range(m):
    queue_len = len(queue)
    idx = queue.index(location[i])
    if idx < queue_len - idx:
        while True:
            if queue[0] == location[i]:
                del queue[0]
                break
            else:
                queue.append(queue[0])
                del queue[0]
                count += 1
    else:
        while True:
            if queue[0] == location[i]:
                del queue[0]
                break
            else:
                queue.insert(0, queue[-1])
                del queue[-1]
                count += 1

print(count)
