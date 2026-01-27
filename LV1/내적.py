# LV1 - 내적 문제의 해답
def solution(a, b):
    """
    :param a: int
    :param b: int
    :return: int
    """
    return sum(x * y for x, y in zip(a, b))