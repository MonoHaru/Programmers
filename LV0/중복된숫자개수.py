# LV0 - 중복된 숫자 개수 문제의 해답
def solution(array: list, n: int) -> int:
    """주어진 배열 array 안에 n이 몇 개 있는지 찾습니다.

    Args:
        array (list[int]): 주어진 정수 배열.
        n (int): 비교 정수.

    Returns:
        int: n의 개수.    
    """
    return array.count(n)

print(solution([1, 1, 2, 3, 4, 5], 1))  # 2
print(solution([0, 2, 3, 4], 1))        # 0