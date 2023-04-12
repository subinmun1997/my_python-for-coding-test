def dfs(cnt, start):
    # 7명의 난쟁이가 선택됐고 합이 100이면
    if cnt == 7:
        if sum(s) == 100:
            # 오름차순으로 정렬해서 출력
            for i in sorted(s):
                print(i)
            # 가능한 정답이 한 가지라도 나왔으면 종료하기
            exit()
        # 7명의 난쟁이의 합이 100이 아니면 해당 경우의 수가 아님
        else:
            return

    for i in range(start, 9):
        s.append(heights[i])
        dfs(cnt+1, i+1)
        s.pop()

# 난쟁이들의 키
heights = [int(input()) for _ in range(9)]

s = []
dfs(0, 0)