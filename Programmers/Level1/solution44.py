def solution(participant, completion):
    participant.sort()
    completion.sort()

    for a, b in zip(participant, completion):
        if a != b:
            return a
    return participant.pop()

print(solution(["leo","kiki","eden"], ["eden","kiki"]))
print(solution(["mislav","stanko","mislav","ana"], ["stanko","ana","mislav"]))