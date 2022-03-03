cow = {}

n = int(input())
count = 0
for _ in range(n):
    cow_number, move = map(int, input().split())
    if cow_number not in cow:
        cow[cow_number] = move
    else:
        if cow[cow_number] != move:
            cow[cow_number] = move
            count += 1

print(count)