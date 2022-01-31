t = int(input())

for _ in range(t):
    n = int(input())
    store = list(map(int, input().split()))
    print((max(store)-min(store))*2)