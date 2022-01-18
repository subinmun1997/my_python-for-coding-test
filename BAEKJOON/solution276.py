s = input()
check_list = ['U','C','P','C']
isSuccess = True

for check in check_list:
    if check in s:
        s = s[s.find(check)+1:]
    else:
        isSuccess = False
        break

if isSuccess:
    print("I love UCPC")
else:
    print("I hate UCPC")