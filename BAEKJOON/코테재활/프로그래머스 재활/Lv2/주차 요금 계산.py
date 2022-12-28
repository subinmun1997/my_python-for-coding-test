import math

def solution(fees, records):
    records.sort(key=lambda x : x.split()[1])
    records.append("24:00 -1-1-1-1 OUT")
    carNum = {}
    for i in range(len(records)):
        time, car, data = records[i].split()
        if data == "OUT": # 출차인 경우에는 직전에 계산 끝냄
            continue
        if records[i+1].split()[1] == car: # 현재 입차이고, 다음차가 동일하며 출차인 경우
            if car in carNum:
                carNum[car] += check_time(time, records[i+1].split()[0])
            else:
                carNum[car] = check_time(time, records[i+1].split()[0])
        else: # 현재 입차인데, 다음차가 동일하지 않다면 마감시간에 23:59 저장
            if car in carNum:
                carNum[car] += check_time(time, "23:59")
            else:
                carNum[car] = check_time(time, "23:59")

    answer = []
    for cnum, total_time in carNum.items():
        if total_time <= fees[0]:
            answer.append(fees[1])
        else:
            cost = fees[1] + math.ceil((total_time - fees[0]) / fees[2]) * fees[3]
            answer.append(cost)

    return answer

def check_time(intime, outtime):
    in_h, in_m = intime.split(":")
    out_h, out_m = outtime.split(":")
    total_in = int(in_h) * 60 + int(in_m)
    total_out = int(out_h) * 60 + int(out_m)
    result = total_out - total_in
    return result

print(solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
print(solution([120, 0, 60, 591], ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]))
print(solution([1, 461, 1, 10], ["00:00 1234 IN"]))