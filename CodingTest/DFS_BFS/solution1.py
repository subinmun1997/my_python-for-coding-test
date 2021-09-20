'''
스택 : 선입후출(First-In-Last-Out)
append() : 리스트의 가장 뒤쪽에 데이터를 삽입
pop() : 리스트의 가장 뒤쪽에서 데이터를 꺼냄
'''

stack = []
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack) # 최하단 원소부터 출력
print(stack[::-1]) # 최상단 원소부터 출력