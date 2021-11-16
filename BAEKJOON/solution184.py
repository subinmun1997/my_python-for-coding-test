s = input()

words = ["C","A","M","B","R","I","D","G","E"]

for i in s:
    if i not in words:
        print(i, end='')