dial = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']

text = input().upper()
time = 0
for i in text:
    for j in dial:
        for k in j:
            if i == k:
                time += dial.index(j) + 3

print(time)
