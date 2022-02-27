t = int(input())

for _ in range(t):
    n, k = map(int, input().split()) # 사탕의 종류, 먹어야되는 사탕의 최소 개수
    candy = list(map(int, input().split()))

    child = 0
    for c in candy:
        child += c//k

    print(child)