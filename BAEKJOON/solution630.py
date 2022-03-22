n = int(input())
l = sorted(list(map(int, input().split())))

chain_len = len(l)
answer, rest = 0, chain_len-1

for i in range(chain_len):
    if l[i] >= rest:
        answer += rest
        break
    else:
        rest -= (l[i] + 1)
        answer += l[i]

print(answer)