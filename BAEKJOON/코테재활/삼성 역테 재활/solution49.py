from collections import Counter

def reverseRowColumn():
    max_len = 0
    for i in range(len(graph)):
        # 수를 정렬할 때 0은 무시해야 한다.
        temp = [k for k in graph[i] if k != 0]
        # {수: 수가 나오는 횟수} 형태로 저장
        temp = Counter(temp).most_common()
        # 수의 등장 횟수가 커지는 순으로(x[1]), 그러한 것이 여러가지면 수가 커지는 순으로(x[0]) 정렬
        temp.sort(key=lambda x : (x[1], x[0]))
        # 정렬된 결과를 저장하기 위해 초기화
        graph[i] = []
        for t in temp:
            graph[i].extend(t)

        # temp 는 (숫자, 등장 횟수) 로 묶여서 있기 때문에 len으로는 1이지만 실제로는 2의 길이를 가짐
        # 그래서 temp_len * 2 처럼 두 배를 해줘야 함
        if max_len < len(temp) * 2:
            max_len = len(temp) * 2

    for j in range(len(graph)):
        # max_len과 해당 행의 길이 차이만큼 0을 추가함
        for k in range(max_len - len(graph[j])):
            graph[j].append(0)
        # 행 또는 열의 크기가 100을 넘어가는 경우에는 처음 100개를 제외한 나머지는 버린다
        graph[j] = graph[j][:100]

# 입력 조건
r, c, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(3)]

for i in range(101):
    # r, c가 범위 내라면
    if r <= len(graph) and c <= len(graph[0]):
        # 해당 칸의 값이 k라면 연산의 최소 시간(i)를 출력하고 끝내기
        if graph[r-1][c-1] == k:
            print(i)
            break

    # 행의 개수 >= 열의 개수 라면 R 연산 수행
    if len(graph) >= len(graph[0]):
        reverseRowColumn()
    else: # 행의 개수 < 열의 개수라면
        graph = list(zip(*graph)) # 전치행렬 수행
        reverseRowColumn() # C 연산 수행
        graph = list(zip(*graph))

else: # 100초가 지나도 graph[r-1][c-1] = k가 되지 않으면 -1 출력
    print(-1)