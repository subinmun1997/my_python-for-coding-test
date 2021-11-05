import sys
n = int(sys.stdin.readline())
card = set(map(int, sys.stdin.readline().split())) # card를 list로 받으면 시간 초과
m = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))

for i in data:
    if i in card:
        print(1)
    else:
        print(0)

'''
시간 복잡도 관점에서 보면, 어떤 원소가 list에 있는지 판별하는 것은 O(n)이고,
set이나 dictionary는 주어진 key를 해쉬를 이용하여 바로 찾기 때문에 O(1)이다.

특정한 데이터 x가 n개의 데이터를 가지고 있는 자료구조 a 안에 들어있는지 알아보는 시간복잡도가
배열(list)는 O(n), 이분 탐색은 O(log n), 집합(set)은 O(1)이다.
이를 m번 반복해야 하므로 시간복잡도는 각각 O(mn), O(m log n), O(m)이다.

또한, 이분 탐색을 하기 위해서는 정렬된 배열이 필요하므로 O(n log n)의 전처리 과정이 필요하며,
그 외 자료구조는 데이터 n개가 들어오는 대로 넣기만 하면 되므로 O(n)의 전처리 과정을 거치는 셈이다.

결론적으로 전체 프로그램의 시간복잡도는
배열은 O(mn), 이분 탐색은 O((m+n) log n), 집합은 O(m+n)이다
'''