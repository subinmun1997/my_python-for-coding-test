question = 0
while True:
    word = input()
    if word == "고무오리 디버깅 끝":
        break

    if word == "문제":
        question += 1
    elif word == "고무오리":
        if question != 0:
            question -= 1
        else:
            question += 2

if question:
    print("힝구")
else:
    print("고무오리야 사랑해")
