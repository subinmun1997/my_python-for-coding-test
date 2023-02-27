while True:
    try:
        s, t = input().split()
        flag = True

        for i in s:
            if i in t:
                t = t[t.index(i)+1:]
            else:
                flag = False
                break
        if flag:
            print("Yes")
        else:
            print("No")

    except:
        break