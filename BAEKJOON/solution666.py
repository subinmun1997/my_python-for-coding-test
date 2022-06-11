temp = float(input())
while True:
    new_temp = float(input())
    if new_temp == 999:
        break
    print(f"{new_temp-temp:.2f}")
    temp = new_temp