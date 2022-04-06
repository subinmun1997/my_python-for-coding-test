n, k = map(int, input().split())
listA = list(map(int, input().split()))
listB = list(map(int, input().split()))

listA.sort() # 배열A는 오름차순 정렬
listB.sort(reverse=True) # 배열B는 내림차순 정렬

for i in range(k):
    if listA[i] < listB[i]: # A의 원소가 B의 원소보다 작은 경우
        listA[i], listB[i] = listB[i], listA[i]
    else:
        break

print(sum(listA))