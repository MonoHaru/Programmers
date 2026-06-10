# LV0 - 제곱수 판별하기 문제의 해답
def solution(n: int) -> int:
    """정수 n이 제곱수인지 확인합니다.

    Args:
        n (int): 주어진 정수.

    Returns:
        int: 제곱수이면 1, 아니면 2.    
    """
    return 1 if (n ** 0.5).is_integer() else 2

print(solution(144))  # 1
print(solution(987))  # 2