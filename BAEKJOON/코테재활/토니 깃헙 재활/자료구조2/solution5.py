tree = dict()

count = 0
while True:
    try:
        name = input()
        count += 1

        if name in tree:
            tree[name] += 1
        else:
            tree[name] = 1
    except:
        break

result = sorted(tree.items(), key=lambda x : x[0])
for k, v in result:
    print("%s %.4f" % (k, round((v / count * 100), 4)))