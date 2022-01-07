m = 1
n = 10001

sosu = set()

a = [True for i in range(n)]

for i in range(2, int(n**0.5)+1):
    if a[i] == True:
        for j in range(i*2,n,i):
            a[j] = False

for i in range(m,n):
    if i>1 and a[i] == True:
        sosu.add(i)

t = int(input())

for k in range(t):
    k = int(input())
    dic = {}

    for i in sosu:
        if k-i in sosu:
            if i <= k-i:
                dic[(k-i)-i] = [i, k-i]
            else:
                dic[i-(k-i)] = [k-i, i]

    key_list = list(dic.keys())
    print(dic[min(key_list)][0], dic[min(key_list)][1])