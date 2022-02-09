import sys
input = sys.stdin.readline

count = 0
fbi = [input() for _ in range(5)]
for f in fbi:
    if 'FBI' in f:
        print(fbi.index(f)+1, end=' ')
        count += 1

if count == 0:
    print("HE GOT AWAY!")