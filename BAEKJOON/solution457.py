n = int(input())
numbers = []

for _ in range(n):
    numbers.append(int(input()))

sub, div = [], []

for i in range(1, n):
    sub.append(numbers[i] - numbers[i-1])
    div.append(numbers[i] // numbers[i-1])

set_sub = list(set(sub))
set_div = list(set(div))

if len(set_sub) == 1:
    print(numbers[-1] + sub[0])
elif len(set_div) == 1:
    print(numbers[-1] * div[0])
