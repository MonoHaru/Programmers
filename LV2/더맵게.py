# LV2 - 더 맵게 문제의 해답
def solution(scoville, K):
    """
    :param scoville: list
    :param K: int
    :return: int
    """
    import heapq
    heapq.heapify(scoville)
    cnt = 0
    
    while scoville[0] < K:
        if len(scoville) < 2:
            return -1
        
        x, y = heapq.heappop(scoville), heapq.heappop(scoville)
        z = x + y * 2
        
        heapq.heappush(scoville, z)
        cnt += 1
        
    return cnt

print(solution([1, 2, 3, 9, 10, 12], 7))  # 2