# LV1 - 예산 문제의 해답
def solution(d, budget):
    """
    :param d: list
    :param budget: int
    :return: int
    """
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)

print(solution([1,3,2,5,4], 9))  # 3
print(solution([2,2,3,3], 10))  # 4