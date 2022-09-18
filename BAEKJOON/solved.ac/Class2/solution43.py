n = int(input())
word = input()

result = 0
for i in range(n):
    result += (int(ord(word[i])) - int(ord('a')) + 1) * (31 ** i)

print(result % 1234567891)