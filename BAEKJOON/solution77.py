while True:
    n = list(map(int, input().split()))
    if sum(n) == 0:
        break
    n.sort(reverse=True)
    if n[0]**2 == (n[1]**2 + n[2]**2):
        print("right")
    else:
        print("wrong")