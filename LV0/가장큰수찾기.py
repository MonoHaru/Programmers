# LV0 - 가장 큰 수 찾기 문제의 해답
def solution(array: list) -> list:
    """가장 큰 수와 그 수의 인덱스를 찾습니다.

    Args:
        array (list): 주어진 리스트.

    Returns:
        list: 가장 큰 수와 인덱스 리스트.    
    """
    return [max(array), array.index(max(array))]

print(solution([1, 8, 3]))       # [8, 1]
print(solution([9, 10, 11, 8]))  # [11, 2]