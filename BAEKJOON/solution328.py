def divisor(num):
    div_list = []
    for i in range(1, num):
        if num%i == 0:
            div_list.append(i)
    return div_list

while True:
    n = int(input())
    if n == -1:
        break
    array = divisor(n)
    if sum(array) == n:
        print(n,"= ",end='')
        for i in range(len(array)-1):
            print(array[i],"+ ",end='')
        print(array[-1])
    else:
        print(n, "is NOT perfect.")

