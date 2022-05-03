a, b, c = map(int, input().split())
array = [a, b, c, a*b, a*c, b*c, a*b*c]

odd = [i for i in array if i%2 != 0]
even = [i for i in array if i%2 == 0]
print(max(odd) if odd else max(even))