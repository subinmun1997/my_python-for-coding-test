import sys
values = {'black':0,'brown':1,'red':2,'orange':3,'yellow':4,'green':5,'blue':6,'violet':7,'grey':8,'white':9}

result = ''
for i in range(3):
    if i != 2:
        n = sys.stdin.readline().rstrip()
        result += str(values[n])
    else:
        n = sys.stdin.readline().rstrip()
        result += ('0' * values[n])

print(int(result))