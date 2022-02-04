n = int(input())

for _ in range(n):
    text = input().lower()
    print("Yes" if text == text[::-1] else "No")