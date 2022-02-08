t = int(input())
for _ in range(t):
    n = int(input())
    pk1 = list(map(str, input().split()))
    pk2 = list(map(str, input().split()))
    ck = list(map(str, input().split()))

    d = {}
    for p in pk2:
        d[pk1.index(p)] = ck.pop(0)

    sorted_dict = " ".join(dict(sorted(d.items())).values())
    print(sorted_dict)
