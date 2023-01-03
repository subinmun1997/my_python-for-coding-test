import math

def solution(m, musicinfos):
    answer = []
    m = m.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")

    for idx, musicinfo in enumerate(musicinfos):
        start, end, title, code = musicinfo.split(",")

        hour, minute = map(int, start.split(":"))
        start = hour * 60 + minute

        hour, minute = map(int, end.split(":"))
        end = hour * 60 + minute
        duration = end - start

        code = code.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")
        code *= math.ceil(duration / len(code))
        code = code[:duration]

        if m in code:
            answer.append([duration, idx, title])

    if not answer:
        return "(None)"
    elif len(answer) == 1:
        return answer[0][2]
    else:
        answer = sorted(answer, key=lambda x : (-x[0], x[1]))
        return answer[0][2]


print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))