t = int(input())

for _ in range(t):
    x1 = input()
    x2 = input()
    count = 0
    for i in range(len(x1)):
        if x1[i] != x2[i]:
            count += 1
    print("Hamming distance is %d." % count)