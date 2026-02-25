# LV2 - 프로세스 문제의 해답
def solution(priorities, location):
    """
    :param priorities: list
    :param location: int
    :return: int
    """
    from collections import deque
    priorities = deque(priorities)
    
    ans = 0
    while True:
        ans += 1
        
        len_q = len(priorities)
        for _ in range(priorities.index(max(priorities))):
            priorities.append(priorities.popleft())
            location = (len_q + location - 1) % len_q
            
        if location == 0:
            return ans
        
        priorities.popleft()
        location -= 1

print(solution([2, 1, 3, 2], 2))  # 1
print(solution([1, 1, 9, 1, 1, 1], 0))  # 5