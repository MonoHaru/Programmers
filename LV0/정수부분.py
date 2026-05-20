# LV0 - 정수 부분 문제의 해답
def solution(flo: float) -> int:
    """실수 flo에서 정수값만 추출한다.

    Args:
        flo (float): 실수.
    
    Returns:
        int: flo에서 정수값.    
    """
    return int(flo)

print(solution(1.42))  # 1
print(solution(69.32))  # 69