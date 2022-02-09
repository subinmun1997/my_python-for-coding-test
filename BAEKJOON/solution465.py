n = int(input())
answer = input()

sang = ['A','B','C'] * 34
chang = ['B','A','B','C'] * 25
hyun = ['C','C','A','A','B','B'] * 17

a_sang = a_chang = a_hyun = 0
for i in range(len(answer)):
    if answer[i] == sang[i]:
        a_sang += 1
    if answer[i] == chang[i]:
        a_chang += 1
    if answer[i] == hyun[i]:
        a_hyun += 1
max_score = max(a_sang, a_chang, a_hyun)
print(max_score)
if max_score == a_sang:
    print("Adrian")
if max_score == a_chang:
    print("Bruno")
if max_score == a_hyun:
    print("Goran")
