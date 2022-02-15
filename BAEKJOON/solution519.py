n = int(input())

for i in range(1, n+1):
    word = list(map(str, input().split()))
    print(f"Case #{i}:", end=' ')
    for j in range(len(word)-1,-1,-1):
        print(word[j], end=' ')
    print()