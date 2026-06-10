# LV0 - 가까운 수 문제의 해답
def solution(array: list, n: int) -> int:
    """정수 배열 array에서 n가 가장 가깝고 작은 수를 찾습니다.

    Args:
        array (list[int]): 정수 리스트.
        n (int): 정수.

    Returns:
        int: 가장 가깝고 작은 수.    
    """
    array.sort()
    
    closest_num = array[0]
    min_diff = abs(array[0] - n)
    
    for m in array:
        current_diff = abs(m - n)
        if current_diff < min_diff:
            min_diff = current_diff
            closest_num = m
            
    return closest_num

print(solution([3, 10, 28], 20))   # 28
print(solution([10, 11, 12], 13))  # 12