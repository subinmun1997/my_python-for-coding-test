import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
answer = []

a_pointer, b_pointer = 0, 0
a_length, b_length = n, m

while a_pointer != a_length or b_pointer != b_length:
    if a_pointer == a_length:
        answer.append(b[b_pointer])
        b_pointer += 1
    elif b_pointer == b_length:
        answer.append(a[a_pointer])
        a_pointer += 1
    else:
        if a[a_pointer] < b[b_pointer]:
            answer.append(a[a_pointer])
            a_pointer += 1
        else:
            answer.append(b[b_pointer])
            b_pointer += 1

print(*answer)
