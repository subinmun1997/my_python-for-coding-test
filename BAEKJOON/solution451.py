t = int(input())
for _ in range(t):
	clothes = {}
	n = int(input())
	for _ in range(n):
		kind, body = map(str, input().split())
		if body in clothes:
			clothes[body] += 1
		else:
			clothes[body] = 1

	values = list(clothes.values())
	result = 1

	for v in values:
		result = result * (v+1)

	print(result-1)