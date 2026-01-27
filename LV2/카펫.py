# LV2 - 카펫 문제의 해답
def solution(brown, yellow):
    """
    :param brown: int
    :param yellow: int
    :return: list
    """
    for i in range(1, yellow + 1):
        if yellow % i == 0:
            x = i + 2
            y = (yellow // i) + 2
            if x * y == brown + yellow:
                return [max(x, y), min(x, y)]
            
print(solution(10, 2))  # [4, 3]
print(solution(8, 1))  # [3, 3]
print(solution(24, 24))  # [8, 6]