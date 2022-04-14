import sys
from collections import defaultdict

input = sys.stdin.readline

count = 0
dict_ = defaultdict(int)
while True:
    n = str(input().rstrip())
    if not n:
        break
    dict_[n] += 1
    count += 1

dict_ = sorted(dict_.items())
for k, v in dict_:
    print("%s %.4f" % (k, round((v/count * 100), 4)))