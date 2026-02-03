# LV2 - 멀리 뛰기 문제의 해답
def solution(n):
    """
    :param n: int
    :return: int
    """
    if n == 1:
        return 1
    elif n == 2:
        return 2
    a, b = 1, 2
    for i in range(2, n):
        a, b = b, a + b
    return b % 1234567

print(solution(4))  # 5
print(solution(3))  # 3