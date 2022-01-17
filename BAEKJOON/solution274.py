n = int(input())

not_cute = 0
cute = 0

for _ in range(n):
    x = int(input())
    if x == 0:
        not_cute += 1
    else:
        cute += 1

if cute > not_cute:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")