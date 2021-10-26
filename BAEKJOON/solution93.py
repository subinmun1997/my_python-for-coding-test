count = int(input())
n= 1
while n < count:
    count-=n
    n+=1

if n%2 == 1:
    print('%d/%d' %(n-count+1,count))
else:
    print('%d/%d' %(count,n-count+1))