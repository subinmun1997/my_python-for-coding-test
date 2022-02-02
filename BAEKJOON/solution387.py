t = int(input())

for _ in range(t):
    str1, str2 = map(str, input().split())
    temp_str1 = sorted(str1)
    temp_str2 = sorted(str2)

    if temp_str1 == temp_str2:
        print(str1, "&", str2, "are anagrams.")
    else:
        print(str1, "&", str2, "are NOT anagrams.")