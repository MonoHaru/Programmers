# LV2 - 피보나치 수 문제의 해답
def solution(n):
    """
    :param n: int
    """
    n_1, n_2 = 1, 0
    for i in range(2, n + 1):
        temp = n_1 + n_2
        n_2 = n_1
        n_1 = temp
    return temp % 1234567

print(solution(3))  # 2
print(solution(5))  # 5