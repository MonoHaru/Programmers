# Lv1 - 최소직사각형
def solution(sizes):
    """
    :param sizes: list
    :return: int
    """
    return max(max(x) for x in sizes) * max(min(y) for y in sizes)

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))  # 4000
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))  # 120
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))  # 133