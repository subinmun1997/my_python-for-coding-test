n = int(input())
o = n%5
if(n==1 or n==3):
  result = -1
elif(o%2==0):
  result = n//5 + o//2
else:
  result = ((n//5)-1) + ((o+5)//2)

print(result)
