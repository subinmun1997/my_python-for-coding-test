'''
List Comprehension : 리스트 안에 for문을 포함
'''

a = [1,2,3,4]
result = []
for num in a:
    result.append(num*3)

print(result)

# 위의 예제를 list comprehension 사용
a = [1,2,3,4]
result = [num*3 for num in a]
print(result)

# 짝수에만 3을 곱하여 담기
a = [1,2,3,4]
result = [num*3 for num in a if num%2 == 0]
print(result)

# 구구단
result = [x*y for x in range(2,10) for y in range(1,10)]
print(result)