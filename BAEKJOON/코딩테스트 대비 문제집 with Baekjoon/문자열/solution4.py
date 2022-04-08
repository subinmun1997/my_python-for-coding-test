t = int(input())
for _ in range(t):
    word_dict = {}
    words = input()

    for word in words:
        if word == ' ':
            continue
        else:
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1

    result = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)
    values = list(word_dict.values())
    max_value = max(values)
    if values.count(max_value) > 1:
        print("?")
    else:
        print(result[0][0])