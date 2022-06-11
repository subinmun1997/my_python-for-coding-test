import math

s = list(int(input()) for _ in range(5))
print(s[0]-max(math.ceil(s[1]/s[3]), math.ceil(s[2]/s[4])))
