t = int(input())

for _ in range(t):
    prime = {}
    n = int(input())

    for i in range(2, n+1):
        while n%i == 0:
            if i in prime:
                prime[i] += 1
            else:
                prime[i] = 1
            n //= i

    for k, v in prime.items():
        print(k, v)