a = [1,4,3]
print("기본 리스트: ", a)

a.append(2)
print("삽입: ", a)

a.sort()
print("오름차순 정렬: ", a)

a.sort(reverse=True)
print("내림차순 정렬: ", a)

a.reverse()
print("원소 뒤집기: ", a)

a.insert(2, 3)
print("인덱스 2에 3 추가: ", a)

print("값이 3인 데이터 개수: ", a.count(3))

a.remove(1)
print("값이 1인 데이터 삭제: ", a)
