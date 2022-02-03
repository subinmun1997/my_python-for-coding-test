nemo = 'nemo'

while True:
    words = input()
    if words == "EOI":
        break
    words = words.lower()
    if nemo in words:
        print("Found")
    else:
        print("Missing")