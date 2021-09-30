alpha = ['c=','c-','dz=','d-','lj','nj','s=','z=']

data = input()

count = 0
for i in alpha:
    if i in data:
        count += data.count(i)
        data =  data.replace(i,'X')


remain = 0
for i in data:
    if i != 'X':
        remain += 1

print(count+remain)