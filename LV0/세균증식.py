# LV0 - 세균 증식 문제의 해답
def solution(n: int, t: int) -> int:
    """n의 2의 t제곱을 계산합니다.

    Args:
        n (int): 주어진 정수.
        t (int): 제곱의 횟수.

    Returns:
        int: 계산값.    
    """
    return n * 2 ** t

print(solution(2, 10))  # 2048
print(solution(7, 15))  # 229376