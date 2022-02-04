for _ in range(3):
    n = input()
    max_len = 0
    count = 1
    for i in range(len(n)-1):
        if n[i] == n[i+1]:
            count += 1
        else:
            max_len = max(max_len, count)
            count = 1
        max_len = max(max_len, count)

    if max_len == 1:
        print(1)
    else:
        print(max_len)