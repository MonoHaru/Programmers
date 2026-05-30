# LV0 - 점의 위치 구하기 문제의 해답
def solution(dot: list) -> int:
    """좌표(dot)가 몇 사분면에 있는지 찾습니다.

    Args:
        dot: 점의 좌표.

    Return:
        int: 사분면 위치.    
    """
    if dot[0] > 0 and dot[1] > 0:
        return 1
    elif dot[0] < 0 and dot[1] > 0:
        return 2
    elif dot[0] < 0 and dot[1] < 0:
        return 3
    else:
        return 4
    
print(solution([2, 4]))   # 1
print(solution([-7, 9]))  # 2