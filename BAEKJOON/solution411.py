mbti = {'E':'I','I':'E','N':'S','S':'N','T':'F','F':'T','J':'P','P':'J'}

result = ''
for i in input():
    result += mbti[i]

print(result)