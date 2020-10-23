n = int(input())

seq = []
for i in range(n):
    seq.append(int(input()))

seq = sorted(seq,reverse=True)

for i in seq:
    print(i, end=' ')