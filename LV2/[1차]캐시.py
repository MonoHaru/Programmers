# LV2 - [1차] 캐시 문제의 해답
def solution(cacheSize, cities):
    """
    :param cacheSize: int
    :param cities: list
    :return: int
    """
    if cacheSize == 0:
        return len(cities) * 5
    
    from collections import deque
    
    que = deque()
    time = 0
    
    for city in cities:
        city = city.lower()
        
        if city in que:
            que.remove(city)
            time += 1
        else:
            if len(que) == cacheSize:
                que.popleft()
            time += 5
            
        que.append(city)
    return time

print(solution(3, 
               ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", 
                "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))  # 50
print(solution(3,
               ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", 
                "Seoul", "Jeju", "Pangyo", "Seoul"]))  # 21
print(solution(2,
               	["Jeju", "Pangyo", "Seoul", "NewYork", 
                 "LA", "SanFrancisco", "Seoul", "Rome", 
                 "Paris", "Jeju", "NewYork", "Rome"]))  # 60
print(solution(5,
               ["Jeju", "Pangyo", "Seoul", "NewYork", 
                "LA", "SanFrancisco", "Seoul", "Rome", 
                "Paris", "Jeju", "NewYork", "Rome"]))  # 52
print(solution(2,
               ["Jeju", "Pangyo", "NewYork", "newyork"]))  # 16
print(solution(0,
               ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))  # 25
