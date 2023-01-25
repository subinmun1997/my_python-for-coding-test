'''
아이디어 정리
* 한 줄 씩 확인해야 하기 때문에 한 줄 기준으로 지나갈 수 있는 길인지 확인하는 함수 작성
* 지나갈 수 있는지 확인하는 함수는 아래 로직을 따른다.
1. 이전 칸과 현재 칸의 높이 차가 1칸 이상이면 False
2. 현재 높이 < 이전 높이; 경사로 설치를 위해 오른쪽 스캔 (낮은 곳에 경사로 설치)
3. 현재 높이 > 이전 높이; 경사로 설치를 위해 왼쪽 스캔 (낮은 곳에 경사로 설치)
'''

def pos(now):
    for j in range(1, n):
        if abs(now[j] - now[j-1]) > 1: # 1.차이가 1만 가능
            return False
        if now[j] < now[j-1]: # 2. 현재 < 이전; 경사로를 만들기 위해 오른쪽 스캔
            for k in range(l): # l 만큼 경사로 너비 필요
                if j+k >= n or used[j+k] or now[j] != now[j+k]: # 범위 넘어감 or 이미 설치함 or 낮은 곳의 높이가 다른 경우 false
                    return False
                if now[j] == now[j+k]: # 높이가 같은 경우 사용 여부 체크
                    used[j+k] = True
        elif now[j] > now[j-1]: # 3. 현재 > 이전; 경사로를 만들기 위해 왼쪽 스캔
            for k in range(l):
                if j-1-k < 0 or now[j-1] != now[j-1-k] or used[j-1-k]: # 범위 넘어감 or 낮은 곳의 높이가 다름 or 이미 설치함 false
                    return False
                if now[j-1] == now[j-1-k]: # 높이가 같은 경우 사용 여부 체크
                    used[j-1-k]
    return True # 모두 문제 없이 설치된 경우 가능함을 리턴

n, l = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
result = 0

#가로 확인
for i in range(n):
    used = [False for _ in range(n)] # 사용 여부
    if pos(graph[i]):
        result += 1

#세로 확인
for i in range(n):
    used = [False for _ in range(n)]
    if pos([graph[j][i] for j in range(n)]):
        result += 1

print(result)