import math
def solution(w,h):
    if w==h:
        return (w*h)-w
    else:
        return (w*h) - (w + h - math.gcd(w,h))

print(solution(8,12))