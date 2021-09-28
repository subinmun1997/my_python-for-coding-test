a = [int(input()) for i in range(10)]

div = [i%42 for i in a]

div = set(div)
print(len(div))