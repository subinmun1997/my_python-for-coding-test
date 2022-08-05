t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    priority = list(map(int, input().split()))
    tf = [False] * m + [True] + [False] * (n-m-1)

    count = 1
    while True:
        if tf[0] and priority[0] == max(priority):
            print(count)
            break
        elif priority[0] == max(priority):
            priority.pop(0)
            tf.pop(0)
            count += 1
        else:
            priority.append(priority.pop(0))
            tf.append(tf.pop(0))
