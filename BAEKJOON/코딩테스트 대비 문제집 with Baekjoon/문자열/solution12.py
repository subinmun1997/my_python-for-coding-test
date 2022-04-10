while True:
    try:
        flag = True
        s, t = input().split()
        for i in s:
            if i in t:
                temp = t.index(i)
                t = t[temp+1:]
            else:
                flag = False
                break
        if flag:
            print("Yes")
        else:
            print("No")
    except:
        break
