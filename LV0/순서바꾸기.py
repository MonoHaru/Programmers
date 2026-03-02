# LV0 - 순서 바꾸기 문제의 해답
def solution(num_list, n):
    """
    :param num_list: list
    :param n: int
    :return: list
    """
    return num_list[n:] + num_list[:n]

print(solution([2, 1, 6], 1))  # [1, 6, 2]
print(solution([5, 2, 1, 7, 5], 3))  # [7, 5, 5, 2, 1]