import sys
n = int(sys.stdin.readline())

array = []
for i in range(n):
    array.append(list(map(str, sys.stdin.readline().rstrip().split())))

result = sorted(array, key=lambda x : (-int(x[1]),int(x[2]),(-int(x[3])), x[0]))

for i in result:
    print(i[0])