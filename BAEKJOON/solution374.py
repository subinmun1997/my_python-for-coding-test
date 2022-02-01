triangle = []
for _ in range(3):
    triangle.append(int(input()))

check = set(triangle)
if len(check) == 1:
    print("Equilateral")
elif len(check) == 2 and sum(triangle) == 180:
    print("Isosceles")
elif len(check) == 3 and sum(triangle) == 180:
    print("Scalene")
elif sum(triangle) != 180:
    print("Error")