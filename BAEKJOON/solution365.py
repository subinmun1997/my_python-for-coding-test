k = int(input())
for i in range(1, k+1):
    math = list(map(int, input().split()))
    n = math.pop(0)
    math.sort(reverse=True)

    diff = []
    for m in range(len(math)-1):
        diff.append(math[m]-math[m+1])
    print("Class %d" %i)
    print("Max %d, Min %d, Largest gap %d" %(max(math), min(math), max(diff)))
