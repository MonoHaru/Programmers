# LV0 - 리스트 자르기 문제의 해답
def solution(n, slicer, num_list):
    """
    :param n: int
    :param slicer: list
    :param num_list: list
    :return: list
    """
    a, b, c = slicer
    if n == 1:
        return num_list[:b+1]
    elif n == 2:
        return num_list[a:]
    elif n == 3:
        return num_list[a:b+1]
    else:
        return num_list[a:b+1:c]

print(solution(3,
               [1, 5, 2],
               [1, 2, 3, 4, 5, 6, 7, 8, 9]))  # [2, 3, 4, 5, 6]
print(solution(4,
               [1, 5, 2],
               [1, 2, 3, 4, 5, 6, 7, 8, 9]))  # [2, 4, 6]