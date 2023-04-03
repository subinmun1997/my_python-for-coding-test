from collections import Counter

def reverseRowColumn():
    max_len = 0
    graph_len = len(graph)
    for i in range(graph_len):
        # 0이 아닌 숫자만 임시 배열에 저장 -> "수를 정렬할 때 0은 무시해야 한다"
        temp = [k for k in graph[i] if k != 0]
        # most_common() -> {원소:횟수}
        temp = Counter(temp).most_common()
        # 정렬 조건 -> 수의 등장 횟수가 커지는 순으로, 그러한 것이 여러가지면 수가 커지는 순으로
        temp.sort(key=lambda x : (x[1], x[0]))
        graph[i] = []
        for t in temp:
            graph[i].extend(t)
        temp_len = len(temp)

        # temp 는 (숫자, 등장 횟수) 로 묶여서 있기 때문에 len으로는 1이지만 실제로는 2의 길이를 가짐
        # 그래서 temp_len * 2 처럼 두 배를 해줘야 함
        if max_len < temp_len * 2:
            max_len = temp_len * 2

    for j in range(graph_len):
        for k in range(max_len - len(graph[j])):
            graph[j].append(0)
        graph[j] = graph[j][:100]

# 입력 조건
# A[r][c]에 들어있는 값이 k가 되기 위한 최소 시간
r, c, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(3)]

# 최소 시간 <= 100
for i in range(101):
    if r <= len(graph) and c <= len(graph[0]):
        # A[r][c] = k라면 시간 출력하고 끝내기
        if graph[r-1][c-1] == k:
            print(i)
            break

    # 행의 개수 >= 열의 개수라면 R연산 수행
    if len(graph) >= len(graph[0]):
        reverseRowColumn()
    # 행의 개수 < 열의 개수라면 C연산 수행
    else:
        # zip함수를 이용한 전치행렬
        graph = list(zip(*graph))
        reverseRowColumn()
        graph = list(zip(*graph))

else:
    print(-1)