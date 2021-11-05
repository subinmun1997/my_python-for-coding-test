import sys
n, m = map(int, sys.stdin.readline().split())

no_listen = set() # 듣도 못한 사람의 수
no_see = set() # 보도 못한 사람의 수

for i in range(n):
    no_listen.add(sys.stdin.readline().rstrip())
for j in range(m):
    no_see.add(sys.stdin.readline().rstrip())

count = 0
count_name = []

for i in no_listen:
    if i in no_see:
        count += 1
        count_name.append(i)

count_name.sort()
print(count)
for i in count_name:
    print(i)
