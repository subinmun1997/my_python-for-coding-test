import sys
input = sys.stdin.readline

a, b = input().split()
x, resulta, resultb = 0, 0, 0
count = 0

for i in range(2, 37):
    try:
        a_temp = int(a, i)
    except:
        continue
    for j in range(2, 37):
        try:
            b_temp = int(b, j)
            if a_temp == b_temp and i != j:
                count += 1
                x = a_temp
                resulta = i
                resultb = j
        except:
            continue

if count == 1:
    print(x, resulta, resultb)
elif count == 0:
    print("Impossible")
else:
    print("Multiple")