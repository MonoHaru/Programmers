# LV0 - 7의 개수 문제의 해답
def solution(array: list) -> int:
    """7의 개수를 구합니다.
    
    Args:
        array (list[int]): 주어진 리스트.

    Return:
        int: 7의 개수.
    """
    return str(array).count('7')

print(solution([7, 77, 17]))  # 4
print(solution([10, 29]))     # 0