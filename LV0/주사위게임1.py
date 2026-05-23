# LV0 - 주사위 게입 1 문제의 해답
def solution(a: int, b: int) -> int:
    """주어진 a, b에 대한 조건에 따라 계산합니다.

    (1) a와 b 모두 홀수면, a^2 + b^2
    (2) a와 b 중 하나가 홀수면, 2 * (a + b)
    (3) a와 b 모두 짝수면, Absolute(a - b)

    Args:
        a (int): 주어진 정수 1.
        b (int): 주어진 정수 2.

    Returns:
        int: 조건에 따라 계산된 결과값.    
    """
    if a % 2 == 1 and b % 2 == 1:
        return a ** 2 + b ** 2
    elif a % 2 == 0 and b % 2 == 0:
        return abs(a - b)
    else:
        return 2 * (a + b)

print(solution(3, 5))  # 34
print(solution(6, 1))  # 14
print(solution(2, 4))  # 2