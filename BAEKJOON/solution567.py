minkook = list(map(int, input().split()))
manse = list(map(int, input().split()))

if sum(minkook) == sum(manse):
    print(sum(minkook))
else:
    print(max(sum(minkook), sum(manse)))