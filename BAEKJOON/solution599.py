n = int(input())
w = sorted(list(map(int, input().split())))

coding = []
for i in range(n):
    temp = w[i] + w[len(w)-i-1]
    coding.append(temp)

print(min(coding))
