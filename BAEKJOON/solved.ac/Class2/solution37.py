import sys
input = sys.stdin.readline

test_num = int(input())

num_list = [0] * 10001
for _ in range(test_num):
    data = int(input())
    num_list[data] += 1

for i in range(1, 10001):
    if num_list[i] != 0:
        for _ in range(num_list[i]):
            print(i)