year, month, day = map(int, input().split())
n_year, n_month, n_day = map(int, input().split())

# 만 나이 / 세는 나이 / 연 나이 출력
if n_year == year:
    print(0)
elif month > n_month:
    print(n_year-year-1)
elif month == n_month and day > n_day:
    print(n_year-year-1)
else:
    print(n_year-year)

print(n_year-year+1)
print(n_year-year)