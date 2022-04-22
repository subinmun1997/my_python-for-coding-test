n = int(input())
result = int(n**0.5)

if result**2 < n:
    print(result+1)
else:
    print(result)
