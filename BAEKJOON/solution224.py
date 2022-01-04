N,L = map(int, input().split())

location = list(map(int,input().split()))
location.sort()

start = 0
cnt=0
for loc in location:
    if start<loc:
        #테이프 붙이기
        # start+L-1 까지는 자동으로 수리됨.
        start = loc+L-1
        cnt+=1

print(cnt)