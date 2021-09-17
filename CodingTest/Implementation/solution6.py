'''
문제 : 럭키 스트레이트

문제 해설 : 정수형 데이터가 입력으로 들어왔을 때, 이를 각 자릿수로 구분하여 합을 계산하면 된다.
            입력받은 데이터가 문자열 형태이므로, 문자열에서 각 문자를 하나씩 확인하며 정수형으로 변환한 뒤에
            그 값을 합 변수에 더할 수 있다.
'''

n = input()
length = len(n) # 점수값의 총 자릿수
summary = 0

# 왼쪽 부분의 자릿수 합 더하기
for i in range(length//2):
    summary += int(n[i])

# 오른쪽 부분의 자릿수 합 빼기
for i in range(length//2, length):
    summary -= int(n[i])

# 왼쪽 부분과 오른쪽 부분의 자릿수 합이 동일한지 검사
if summary == 0:
    print("LUCKY")
else:
    print("READY")