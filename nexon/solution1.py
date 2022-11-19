def minNum(samDaily, kellyDaily, difference):
    dayCount = 0
    sam = difference
    kelly = 0
    if samDaily == kellyDaily and difference == 0:
        return -1
    while True:
        if sam < kelly:
            break
        sam += samDaily
        kelly += kellyDaily
        dayCount += 1
    return dayCount

result = minNum(100, 100, 0)
print(result)

result = minNum(4, 5, 1)
print(result)