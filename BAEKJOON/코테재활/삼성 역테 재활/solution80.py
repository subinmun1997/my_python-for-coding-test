# 입력 값
n = int(input())
nums = list(map(int, input().split()))
# + 개수, - 개수, * 개수, // 개수
op = list(map(int, input().split()))

# 최댓값
max_value = -int(1e9)
# 최솟값
min_value = int(1e9)

def dfs(depth, total, plus, minus, multiply, divide):
    global max_value, min_value

    # 연산자의 개수만큼 dfs 탐색을 했다면
    # 최댓값과 최솟값 구하고 리턴하기
    if depth == n:
        max_value = max(max_value, total)
        min_value = min(min_value, total)
        return

    if plus:
        dfs(depth+1, total + nums[depth], plus-1, minus, multiply, divide)
    if minus:
        dfs(depth+1, total - nums[depth], plus, minus-1, multiply, divide)
    if multiply:
        dfs(depth+1, total * nums[depth], plus, minus, multiply-1, divide)
    if divide:
        dfs(depth+1, int(total / nums[depth]), plus, minus, multiply, divide-1)

dfs(1, nums[0], op[0], op[1], op[2], op[3])
print(max_value)
print(min_value)