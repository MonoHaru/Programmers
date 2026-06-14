# LV0 - 삼각형의 완성조건 (2) 문제의 해답
def solution(sides: list) -> int:
    """삼각형을 만들 수 있는 경우의 수를 구합니다.

    짧은 두 변의 길이는 가장 긴 변의 길이보다 길어야 합니다.

    Args:
        sides (list[int]): 변 길이 정수 리스트.

    Returns:
        int: 삼각형을 만들 수 있는 경우의 수.    
    """
    min_s, max_s = min(sides), max(sides)
    l1 = len(range(max_s - min_s + 1, max_s))
    l2 = len(range(max_s, min_s + max_s))
    return l1 + l2

print(solution([1, 2]))   # 1
print(solution([3, 6]))   # 5
print(solution([11, 7]))  # 13