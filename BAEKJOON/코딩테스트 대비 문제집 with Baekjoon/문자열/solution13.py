import re

p = re.compile('^[ABCDEF]{0,1}A+F+C+[ABCDEF]{0,1}$')

for _ in range(int(input())):
    print("Infected!" if p.match(input()) else 'Good')