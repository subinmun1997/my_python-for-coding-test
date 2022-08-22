from collections import Counter

word = input().upper()
counter = Counter(word)
counting_arr = counter.most_common(n=2)
if len(counter) == 1:
    print(word)
elif counting_arr[0][1] == counting_arr[1][1]:
    print('?')
else:
    print(counting_arr[0][0])