import sys
m = int(sys.stdin.readline())

s = set([])

for i in range(m):
    data = sys.stdin.readline().rstrip().split()
    if data[0] == "add":
        s.add(data[1])
    elif data[0] == "remove":
        s.discard(data[1])
    elif data[0] == "check":
        st = set([data[1]])
        temp_set = st&s
        if len(temp_set) == 1:
            print(1)
        else:
            print(0)
    elif data[0] == "toggle":
        st = set([data[1]])
        temp_set = st&s
        if len(temp_set) == 1:
            s.discard(data[1])
        else:
            s.add(data[1])
    elif data[0] == "all":
        s = set({'1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'})
    elif data[0] == "empty":
        s = set([])
