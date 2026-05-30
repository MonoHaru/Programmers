# LV0 - 공 던지기 문제의 해답
def solution(numbers: list, k: int) -> int:
    """순환하며 2간격으로 공 던잘 때, k번째 던지를 위치를 찾습니다.

    Args:
        numbers (list[int]): 던지는 순서.
        k (int): 던지는 횟수.

    Returns:
        int: k번째 던지는 순서.
    """
    return numbers[(k - 1) * 2 % len(numbers)]

print(solution([1, 2, 3, 4], 2))        # 3
print(solution([1, 2, 3, 4, 5, 6], 5))  # 3
print(solution([1, 2, 3], 3))           # 2