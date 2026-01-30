# LV2 - 점프와 순간 이돈
def solution(n):
    """
    :param n: int
    :return: int
    """
    return bin(n).count("1")

print(solution(5))  # 2
print(solution(6))  # 2
print(solution(5000))  # 5