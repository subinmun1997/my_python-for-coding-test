def check_budget(budget, m, start, end):
    while start <= end:
        mid = (start + end) // 2
        total = 0
        for i in budget:
            if mid < i:
                total += mid
            else:
                total += i
        if total <= m:
            start = mid + 1
        else:
            end = mid - 1
    return end

n = int(input())
budget = sorted(list(map(int, input().split())))
m = int(input())

if sum(budget) <= m:
    print(max(budget))
else:
    answer = check_budget(budget, m, 1, max(budget))
    print(answer)