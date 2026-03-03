# LV0 - n 번째 원소까지
def solution(num_list, n):
    """
    :param num_list: list,
    :param n: int
    :return: list
    """
    return num_list[:n]

print(solution([2, 1, 6], 1))  # [2]
print(solution([5, 2, 1, 7, 5], 3))  # [5, 2, 1]