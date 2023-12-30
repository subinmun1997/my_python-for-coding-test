t = int(input())

for _ in range(t):
    arr = [int(input()) for _ in range(int(input()))]

    max_v = max(arr)
    if arr.count(max_v) > 1:
        print("no winner")
    elif max_v > sum(arr) // 2:
        print("majority winner", arr.index(max_v)+1)
    else:
        print("minority winner", arr.index(max_v)+1)