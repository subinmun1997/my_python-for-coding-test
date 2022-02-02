Soongsil, Korea, Hanyang = map(int, input().split())

if Soongsil+Korea+Hanyang >= 100:
    print("OK")
else:
    min_value = min(Soongsil, Korea, Hanyang)
    if min_value == Soongsil:
        print("Soongsil")
    elif min_value == Korea:
        print("Korea")
    else:
        print("Hanyang")