# LV2 - 더 맵게 문제의 해답
def solution(scoville, K):
    """
    Before:
        - List에서 정렬 후 사용
        - 시간 복잡도 O(n^2 log n)
    After:
        - 최소값들을 사용한 방법으로 Heap 구조 사용
        - 시간 복잡도 O(n log n)
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