alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

n = input()

for i in alpha:
    if i in n:
        print(n.index(i), end=' ')
    else:
        print("-1", end=' ')