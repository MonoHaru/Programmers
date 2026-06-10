# LV0 - 머쓱이보다 키 큰 사람 문제의 해답
def solution(array: list, height: int) -> int:
    """주어진 키 height보다 큰 키의 개수를 찾습니다.

    Args:
        array (list[int]): 주어진 키 정수 배열.
        height (int): 비교값.

    Returns:
        int: height보다 큰 개수.    
    """
    return sum([1 for h in array if h > height])

print(solution([149, 180, 192, 170], 167))  # 3
print(solution([180, 120, 140], 190))       # 0