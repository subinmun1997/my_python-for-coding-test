def factorial(x):
    if x <= 1:
        return 1
    return x * factorial(x-1)


def e(n):
    f_sum = 0
    for i in range(n+1):
       f_sum += 1 / factorial(i)
    return f_sum


print("n e")
print("- -----------")
for i in range(10):
    if i <= 1:
        print(f"{i} {e(i):.0f}")
    elif i == 2:
        print(f"{i} {e(i):.1f}")
    else:
        print(f"{i} {e(i):.9f}")