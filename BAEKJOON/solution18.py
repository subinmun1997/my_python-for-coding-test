def his(i) :
    while(len(s)!=0 and a[s[-1]]>a[i]) :
        idx=s.pop()
        if(len(s)==0) : ans.append(a[idx]*(i-1))
        else : ans.append(a[idx]*((i-1)-s[-1]))

while True :
    a=[*map(int, input().split())]
    n=a[0]
    if(n==0) : break
    s=[]
    ans=[]
    for i in range(1, n+1) :
        if(i!=1 and a[i-1]>a[i]) :
            his(i)
        s.append(i)
    for i in range(len(s)) :
        idx=s.pop()
        if(len(s)==0) : ans.append(a[idx]*n)
        else : ans.append(a[idx]*(n-s[-1]))
    print(max(ans))