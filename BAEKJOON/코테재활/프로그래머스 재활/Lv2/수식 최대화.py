from itertools import permutations

def operation(num1, num2, op):
    if op == "+":
        return str(int(num1) + int(num2))
    if op == "-":
        return str(int(num1) - int(num2))
    if op == '*':
        return str(int(num1) * int(num2))

def calculate(exp, op):
    array = []
    temp = ''
    for i in exp:
        if i.isdigit():
            temp += i
        else:
            array.append(temp)
            array.append(i)
            temp = ''
    array.append(temp)

    for o in op:
        stack = []
        while len(array):
            temp = array.pop(0)
            if temp == o:
                stack.append(operation(stack.pop(), array.pop(0), o))
            else:
                stack.append(temp)

        array = stack
    return abs(int(array[0]))


def solution(expression):
    op = ['-', '*', '+']

    result = []
    for i in permutations(op, 3):
        result.append(calculate(expression, i))

    return max(result)

print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))