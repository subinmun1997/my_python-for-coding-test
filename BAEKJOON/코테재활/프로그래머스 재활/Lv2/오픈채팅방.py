def solution(record):
    nick = {}
    inout = []
    for i in record:
        if "Enter" in i:
            data, id, name = i.split()
            inout.append((data, id))
            nick[id] = name
        elif "Leave" in i:
            data, id = i.split()
            inout.append((data, id))
        elif "Change" in i:
            data, id, name = i.split()
            nick[id] = name

    answer = []
    for x, y in inout:
        if x == "Enter":
            answer.append(nick[y] + "님이 들어왔습니다.")
        else:
            answer.append(nick[y] + "님이 나갔습니다.")

    return answer


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))