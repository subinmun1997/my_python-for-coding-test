def solution(record):
    array = [] # 출입 리스트
    nickname = {} # key: id, value: 닉네임
    answer = []

    for r in record:
        if "Enter" in r:
            enter, id, nick = r.split()
            array.append((enter, id))
            nickname[id] = nick
        elif "Leave" in r:
            enter, id = r.split()
            array.append((enter, id))
        elif "Change" in r:
            enter, id, nick = r.split()
            array.append((enter, id))
            nickname[id] = nick

    for enter, id in array:
        if enter == "Enter":
            temp = nickname[id] + "님이 들어왔습니다."
            answer.append(temp)
        elif enter == "Leave":
            temp = nickname[id] + "님이 나갔습니다."
            answer.append(temp)

    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))
