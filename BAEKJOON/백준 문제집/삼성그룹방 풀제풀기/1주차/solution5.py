from itertools import combinations

def check(word):
    v = 'aeiou'
    # 사용된 모음 개수
    vcnt = 0

    for w in word:
        if w in v:
            vcnt += 1
    # 사용된 모음이 1개 이상, 자음이 2개 이상이라면 true
    return vcnt >= 1 and len(word) - vcnt >= 2

# 입력 조건
l, c = map(int, input().split())
alpha = list(map(str, input().split()))

word = set()
for comb in combinations(alpha, l):
    temp = ''.join(sorted(comb))
    #최소 한 개의 모음과 최소 두 개의 자음으로 구성됐다면
    if check(temp):
        word.add(temp)

# 사전순 출력
for i in sorted(word):
    print(i)