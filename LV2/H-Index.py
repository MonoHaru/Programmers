# LV2 - H-Index 문제의 해답
def solution(citations):
    """
    :param citations: list
    :return: int
    """
    citations.sort()
    n = len(citations)
    ans = 0
    for i, c in enumerate(citations):
        ans = max(ans, min(c, n - i))
    return ans

print(solution([3, 0, 6, 1, 5]))  # 3