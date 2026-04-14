# LV0 - 길이에 따른 연산 문제의 해답
def solution(num_list):
    """
    :param num_list: list
    :return: int
    """
    from math import prod
    return sum(num_list) if len(num_list) >= 11 else prod(num_list)

print(solution([3, 4, 5, 2, 5, 4, 6, 7, 3, 7, 2, 2, 1]))  # 51
print(solution([2, 3, 4, 5]))  # 120