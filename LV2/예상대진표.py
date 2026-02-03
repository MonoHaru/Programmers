# LV2 - 예상 대진표 문제의 해답
def solution(n,a,b):
    """
    :param n: int
    :param a: int
    :param b: int
    :return: int
    """
    cnt = 0
    while a != b:
        a, b = (a + 1) // 2, (b + 1) // 2
        cnt += 1
    return cnt

print(solution(8, 4, 7))  # 3