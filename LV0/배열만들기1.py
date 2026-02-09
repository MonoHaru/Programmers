# LV0 - 배열 만들기 1 문제의 해답
def solution(n, k):
    """
    :param n: int
    :param k: int
    :return: list
    """
    return list(range(k, n+1, k))

print(solution(10, 3))  # [3, 6, 9]
print(solution(15, 5))  # [5, 10, 15]