vowels = ['A','E','I','O','U','a','e','i','o','u']

while True:
    words = input()
    if words == '#':
        break
    count = 0
    for word in words:
        if word in vowels:
            count += 1
    print(count)