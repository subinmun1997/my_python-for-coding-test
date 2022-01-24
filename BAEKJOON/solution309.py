from itertools import combinations
import sys

input = sys.stdin.readline

def make_code():
    result = []
    for c in list(combinations(array, l)):
        vowel_count = consonants_count = 0
        for char in c:
            if char in vowels:
                vowel_count += 1
            else:
                consonants_count += 1
        if vowel_count >= 1 and consonants_count >= 2:
            result.append("".join(c))
    return result
l, c = map(int, input().split())
array = sorted(input().split())

vowels =  ['a','e','i','o','u']

for p in make_code():
    print(p)