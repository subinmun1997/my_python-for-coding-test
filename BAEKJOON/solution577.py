while True:
    try:
        s, t = map(str, input().split())
        temp = ''
        for alpha  in s:
            if alpha in t:
                temp += alpha
                t_idx = t.index(alpha)
                t = t[t_idx+1:]

        if s == temp:
            print("Yes")
        else:
            print("No")
    except:
        exit()

