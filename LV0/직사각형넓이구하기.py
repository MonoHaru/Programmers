# LV0 - 직사각형 넓이 구하기 문제의 해답
def solution(dots: list) -> int:
    """좌표 리스트 dots의 넓이를 구하시오.

    Args:
        dots (list[int]): 좌표 정수 리스트.

    Returns:
        int: 직사각형 넓이.    
    """
    dots.sort()
    dx = abs(dots[0][0] - dots[2][0])
    dy = abs(dots[0][1] - dots[1][1])
    return dx * dy

print(solution([[1, 1], [2, 1], [2, 2], [1, 2]]))      # 1
print(solution([[-1, -1], [1, 1], [1, -1], [-1, 1]]))  # 4