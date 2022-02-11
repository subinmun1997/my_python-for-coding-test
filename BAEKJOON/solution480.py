n = int(input())
for i in range(1, n+1):
    a, b, c = sorted(map(int, input().split()))

    if c**2 == (a**2 + b**2):
        print(f"Scenario #{i}:")
        print("yes")
    else:
        print(f"Scenario #{i}:")
        print("no")
    print()