import sys
input = sys.stdin.readline

n = int(input())
cranes = sorted(list(map(int, input().split())), reverse=True)
m = int(input())
boxs = sorted(list(map(int, input().split())), reverse=True)

if cranes[0] < boxs[0]:
    print(-1)
    exit()
else:
    answer = 0
    while boxs:
        for crane in cranes:
            for box in boxs:
                print(crane, box)
                print(boxs)
                if crane >= box:
                    boxs.remove(box)
                    break

        answer += 1

print(answer)



