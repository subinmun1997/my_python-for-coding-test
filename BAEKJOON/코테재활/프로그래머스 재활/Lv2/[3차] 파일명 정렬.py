def solution(files):
    temp = []
    head, number, tail = '', '', ''

    for file in files:
        for i in range(len(file)):
            if file[i].isdigit():
                head = file[:i]
                number = file[i:]

                for j in range(len(number)):
                    if not number[j].isdigit():
                        tail = number[j:]
                        number = number[:j]
                        break

                temp.append([head, number, tail])
                head, number, tail = '', '', ''
                break

    temp = sorted(temp, key=lambda x : (x[0].lower(), int(x[1])))

    return [''.join(i) for i in temp]

print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))