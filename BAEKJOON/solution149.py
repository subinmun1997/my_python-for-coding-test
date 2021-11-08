n = int(input())
fibo = []

for i in range(41):
  if i ==0: fibo.append([1,0])
  elif i==1: fibo.append([0,1])
  else:
    fibo.append([fibo[i-1][0]+fibo[i-2][0], fibo[i-1][1]+fibo[i-2][1]])

for i in range(n):
  index = int(input())
  print(fibo[index][0], fibo[index][1])