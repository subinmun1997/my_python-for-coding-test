n = input()

left = right = 0
for i in range(len(n)//2): # 왼쪽 반
    left += int(n[i])

for i in range(len(n)//2, len(n)): # 오른쪽 반
    right += int(n[i])

print("LUCKY" if left == right else "READY")