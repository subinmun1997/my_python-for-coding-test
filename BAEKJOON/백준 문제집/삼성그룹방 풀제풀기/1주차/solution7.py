def solution(numbers):
    for i in range(len(numbers)):
        # 큰 수 구하기
        max_value = '7' * (numbers[i] % 2) + '1' * (numbers[i] // 2 - (numbers[i] % 2))

        # 작은 수 구하기
        ans = [0, 0, 1, 7, 4, 2, 6, 8, 10, 18, 22]
        n = numbers[i]
        if n <= 10:
            min_value = ans[n]
        else:
            min_value = ''
            while n > 0:
                n -= 7
                if n >= 0:
                    min_value += '8'
                else:
                    n += 7
                    break
            small = {2:'1', 5:'2', 6:'6'}
            if n in small:
                min_value = small[n] + min_value
            else:
                if n == 1:
                    min_value = '10' + min_value[1:]
                elif n == 3:
                    min_value = '200' + min_value[2:]
                elif n == 4:
                    min_value = '20' + min_value[1:]

        print(min_value, end=' ')
        print(max_value)

n = int(input())
numbers = [int(input()) for _ in range(n)]
solution(numbers)