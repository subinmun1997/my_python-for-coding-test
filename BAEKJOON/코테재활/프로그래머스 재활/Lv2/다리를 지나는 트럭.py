def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_on_bridge = [0 for _ in range(bridge_length)]

    while len(truck_on_bridge):
        answer += 1
        truck_on_bridge.pop(0)
        bridge_weight = sum(truck_on_bridge)

        if truck_weights:
            if bridge_weight + truck_weights[0] <= weight:
                truck_on_bridge.append(truck_weights.pop(0))
            else:
                truck_on_bridge.append(0)

    return answer

print(solution(2, 10, [7,4,5,6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))