def solution(participant, completion):
    participant.sort()
    completion.sort()

    for a, b in zip(participant, completion):
        if a != b:
            return a
    return participant[-1]

print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))