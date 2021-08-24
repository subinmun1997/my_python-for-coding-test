def solution(phone_book):
    answer = True
    phone_book.sort()
    for p1,p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False
    return answer

print(solution(["119","97674223","1195524421"]))
print(solution(["123","456","789"]))
print(solution(["12","123","1235","567","88"]))