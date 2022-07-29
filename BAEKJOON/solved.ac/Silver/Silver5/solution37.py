import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a_pointer, b_pointer = 0, 0
a_length, b_lenght = n, m
result = []

while a_pointer != a_length or b_pointer != b_lenght:
    if a_pointer == a_length:
        result.append(b[b_pointer])
        b_pointer += 1
    elif b_pointer == b_lenght:
        result.append(a[a_pointer])
        a_pointer += 1
    else:
        if a[a_pointer] < b[b_pointer]:
            result.append(a[a_pointer])
            a_pointer += 1
        else:
            result.append(b[b_pointer])
            b_pointer += 1

print(*result)




