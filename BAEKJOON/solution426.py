n = int(input())

for _ in range(n):
    words = input().split()
    print(' '.join(words[2:]+words[:2]))