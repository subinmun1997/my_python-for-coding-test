t = int(input())

for _ in range(t):
    scores = sorted(list(map(int, input().split())))[1:-1]
    if max(scores)-min(scores) >= 4:
        print("KIN")
    else:
        print(sum(scores))