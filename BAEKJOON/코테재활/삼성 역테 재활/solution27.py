# 입력 조건
n = int(input())
nums = list(map(int, input().split()))
op = list(map(int, input().split()))

# 출력 대상 (최댓값, 최솟값)
min_value = 1e9
max_value = -1e9

def dfs(depth, total, plus, minus, multiply, divide):
    global min_value, max_value

    # depth가 숫자의 개수(n)과 같으면 최대, 최소 구해서 리턴하기
    if depth == n:
        min_value = min(min_value, total)
        max_value = max(max_value, total)
        return

    # dfs돌며 depth를 하나 증가시켜주고 total에 해당 depth index의 숫자를 계산하고, 해당하는 연산자 -1해주기
    if plus:
        dfs(depth + 1, total + nums[depth], plus - 1, minus, multiply, divide)
    if minus:
        dfs(depth + 1, total - nums[depth], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(depth + 1, total * nums[depth], plus, minus, multiply - 1, divide)
    if divide:
        dfs(depth + 1, int(total / nums[depth]), plus, minus, multiply, divide - 1)

dfs(1, nums[0], op[0], op[1], op[2], op[3])
print(max_value)
print(min_value)

