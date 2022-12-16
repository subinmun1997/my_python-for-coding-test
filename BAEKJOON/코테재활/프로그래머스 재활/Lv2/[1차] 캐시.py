from collections import deque

def solution(cacheSize, cities):
    queue = deque()
    time = 0
    for city in cities:
        city = city.lower()
        if cacheSize == 0:
            time = len(cities) * 5
            break
        if city in queue:
            queue.remove(city)
            queue.append(city)
            time += 1
        else:
            if len(queue) >= cacheSize:
                queue.popleft()
                queue.append(city)
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