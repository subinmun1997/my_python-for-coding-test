import math

n = int(input())

for i in range(n):
    print('* '*(math.floor(1+((n-1)/2))))
    print(' *'*(math.ceil((n-1)/2)))