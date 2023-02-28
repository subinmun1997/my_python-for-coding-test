import re

p = re.compile('^[A-F]{0,1}A+F+C+[A-F]{0,1}$')


for _ in range(int(input())):
    print("Infected!" if p.match(input()) else 'Good')