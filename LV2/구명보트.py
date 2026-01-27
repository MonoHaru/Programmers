# LV2 - 구명보트 문제의 해답
def solution(people, limit):
    """
    :param people: list
    :param limit: int
    :return: int
    """
    people.sort()
    
    cnt = 0
    light = 0
    heavy = len(people) - 1
    while light < heavy:
        if people[light] + people[heavy] <= limit:
            light += 1
            cnt += 1
        heavy -= 1
        
        if light == heavy:
            break
    return len(people) - cnt

print(solution([70, 50, 80, 50], 100))  # 3
print(solution([70, 80, 50], 100))  # 3