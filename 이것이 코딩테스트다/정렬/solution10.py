array = [('바나나', 2), ('사과', 5), ('당근', 3)]

result = sorted(array, key=lambda x : x[1])
print(result)