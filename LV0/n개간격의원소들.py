# LV0 - n개 간격의 원소들
def solution(num_list, n):
    """
    :param num_list: list
    :param n: int
    :return: list
    """
    return num_list[::n]

print(solution([4, 2, 6, 1, 7, 6], 2))  # [4, 6, 7]
print(solution([4, 2, 6, 1, 7, 6], 4))  # [4, 7]