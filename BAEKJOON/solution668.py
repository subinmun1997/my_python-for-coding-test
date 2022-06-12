t = int(input())
for _ in range(t):
    num = int(input())
    num += int(str(num)[::-1])
    print("YES" if num == int(str(num)[::-1]) else "NO")