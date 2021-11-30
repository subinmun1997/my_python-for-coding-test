w, k = [], []
for i in range(10):
    w.append(int(input()))

for i in range(10):
    k.append(int(input()))

w.sort(reverse=True)
k.sort(reverse=True)

total_w, total_k = 0, 0
for i in range(3):
    total_w += w[i]
    total_k += k[i]

print(total_w, total_k)