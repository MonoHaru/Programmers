# LV1 - 삼총사 문제의 해답
def solution(number):
    """
    :param number: list
    :return: int
    """
    from itertools import combinations
    cnt = 0
    for nums in combinations(number, 3):
        if sum(nums) == 0:
            cnt += 1
    return cnt

print(solution([-2, 3, 0, 2, -5]))  # 2
print(solution([-3, -2, -1, 0, 1, 2, 3]))  # 5
print(solution([-1, -1, -1, 1]))  # 0