# LV0 - 구슬을 나누는 경우의 수 문제의 해답
def solution(balls: int, share: int) -> int:
    """전체 공의 수(balls)에서 share 개를 나누는 경우의 수를 구합니다.

    Args:
        balls (int): 전체 공 개수.
        share (int): 가져갈 공 개수.

    Returns:
        int: 가져가는 공의 경우의 수.    
    """
    n = 1
    for i in range(balls, balls - share, -1):
        n *= i
    
    m = 1
    for i in range(share, 0, -1):
        m *= i

    return n / m

print(solution(3, 2))  # 3
print(solution(5, 3))  # 10