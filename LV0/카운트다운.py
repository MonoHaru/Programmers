# LV0 - 카운트 다운 문제의 해답
def solution(start_num, end_num):
    """
    :param start_num: int
    :param end_num: int
    :return: list
    """
    return list(range(start_num, end_num-1, -1))

print(solution(10, 3))  # [10, 9, 8, 7, 6, 5, 4, 3]