# LV0 - 삼각형의 완성조건 (1) 문제의 해답
def solution(sides: list) -> int:
    """삼각형이 되는지 안되는지 확인합니다.

    Args:
        sides (list[int]): 삼각형 세 변의 길이.

    Returns:
        int: 삼각형이 되면 1, 아니면 2를 반환.    
    """
    sides.sort()
    return 1 if sides[0] + sides[1] > sides[2] else 2