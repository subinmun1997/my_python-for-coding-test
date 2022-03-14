word = list(input())
result = [''] * len(word)

def check(arr, start):
    if not arr:
        return
    min_value = min(arr)
    idx = arr.index(min_value)
    result[start+idx] = min_value
    print("".join(result))
    check(arr[idx+1:], start+idx+1)
    check(arr[:idx], start)

check(word, 0)