n = int(input()) # 토핑의 종류
dough, toping = map(int, input().split())
cal_dough = int(input())
cal_toping = [int(input()) for _ in range(n)]
cal_toping.sort(reverse=True)

total_cal = []
total_cal.append(cal_dough // dough)
for i in range(n):
    temp = cal_toping[:i+1]
    result = (cal_dough + sum(temp)) // (dough + toping * (i+1))
    total_cal.append(result)

print(max(total_cal))
