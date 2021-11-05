n = int(input())

array = []
for i in range(n):
    input_data = input().split()
    array.append((i,int(input_data[0]), input_data[1]))

array.sort(key=lambda x:(x[1],i))

for i in array:
    print(i[1],i[2])