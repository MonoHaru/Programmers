# LV1 - 수박수박수박수박수박수? 문제의 해답
def solution(n):
    """
    :param n: int
    :return: str
    """
    str = '수박' * (n // 2 + 1)
    return str[:n]

print(solution(3))  # "수박수"
print(solution(4))  # "수박수박"