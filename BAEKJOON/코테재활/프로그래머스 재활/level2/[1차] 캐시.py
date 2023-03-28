'''
deque의 생성자에 maxlen을 전달해줄 수 있고, deque가 maxlen 값 만큼만
객체를 가지고 있을 수 있게 된다. 만약 객체의 수가 maxlen에 도달한 상태에서
deque에 새 객체를 삽입(append)하면, 가장 왼쪽에 있는 객체가 제거된 후에 새 객체가 삽입된다.
(반대로 appendleft하면 가장 오른쪽에 있는 객체가 제거된 후에 새 객체가 삽입된다.)
'''
from collections import deque

def solution(cacheSize, cities):
    queue = deque(maxlen=cacheSize)

    time = 0
    for city in cities:
        city = city.lower()
        if city in queue:
            queue.remove(city)
            queue.append(city)
            time += 1
        else:
            queue.append(city)
            time += 5

    return time

print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))
print(solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
print(solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))
print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))
print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))