pocket = ['paper','cellphone','money']

if 'money' in pocket:
    print("택시를 타고 가라")
else:
    print("걸어 가라")

if 'card' not in pocket:
    print("걸어 가라")
else:
    print("버스를 타고 가라")

# 조건문에서 아무 일도 하지 않게 설정하고 싶다면 pass 사용

if 'money' in pocket:
    pass
else:
    print("카드를 꺼내라")