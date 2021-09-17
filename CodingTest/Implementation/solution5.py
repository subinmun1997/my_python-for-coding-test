n = int(input())
temp = str(n)

result1 = 0
result2 = 0
mid =  len(temp) // 2
for i in range(mid):
    result1 += int(temp[i])

for i in range(mid,len(temp)):
    result2 += int(temp[i])

if result1 == result2:
    print("LUCKY")
else: 
    print("READY")