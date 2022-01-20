n, m, k = map(int, input().split())

team = 0
while True:
    n -= 2
    m -= 1
    if n >= 0 and m >= 0 and n+m >= k :
        team += 1
    else:
        break

print(team)
