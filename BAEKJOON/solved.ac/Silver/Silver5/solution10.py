word = input()
croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

count = 0
for i in croatia:
    word = word.replace(i, '0')

print(len(word))