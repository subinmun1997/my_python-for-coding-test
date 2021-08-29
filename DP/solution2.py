'''
메모이제이션: 다이나믹 프로그래밍을 구현하는 방법 중 한 종류로, 한 번 구한 결과를
메모리 공간에 메모해두고 같은 식을 다시 호출하면 메모한 결과를 그대로 가져오는 기법
'''


d = [0] * 100

def fibo(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0: # 이미 계산한 적 있는 문제라면 그대로 반환
        return d[x]
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(99))