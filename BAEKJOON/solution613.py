def add_star(ptn):
    return "* " + ptn + " *"

def star(n):
    if n == 1:
        return ["*"]
    else:
        return ["*"*(4*n-3), "*"+" "*(4*n-5)+"*"]\
                + list(map(add_star, star(n-1)))\
                + ["*"+" "*(4*n-5)+"*", "*"*(4*n-3)]

print("\n".join(star(int(input()))))