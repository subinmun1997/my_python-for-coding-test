year = int(input())

leaf = ((year%4==0) and (year%100!=0)) or (year%400==0)
if leaf:
    print("1")
else:
    print("0")