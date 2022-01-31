t = int(input())
for _ in range(t):
    data = list(map(int, input().split()))
    even = [i for i in data if i%2==0]

    print(sum(even), min(even))