duck = input()
visited = [False] * len(duck)
word = 'quack'

idx = 0
count = 0

if len(duck)%5 != 0 or len(duck) < 5:
    print(-1)
    exit()

for i in range(len(duck)):
    if duck[i] == 'q' and not visited[i]:
        flag = True

        for j in range(i, len(duck)):
            if duck[j] == word[idx] and not visited[j]:
                visited[j] = True

                if duck[j] == 'k':
                    if flag:
                        count += 1
                        flag = False
                    idx = 0
                    continue
                idx += 1

if not all(visited) or count == 0:
    print(-1)
else:
    print(count)
                