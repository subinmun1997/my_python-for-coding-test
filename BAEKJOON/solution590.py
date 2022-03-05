n, m = map(int, input().split()) # 책 개수, 박스 무게
if n == 0:
    print(0)
else:
    book_weight = list(map(int, input().split()))
    box_count = 1
    temp = 0
    for i in range(n):
        temp += book_weight[i]
        if temp > m:
            box_count += 1
            temp = book_weight[i]
    print(box_count)