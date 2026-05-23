# LV0 - 정수 찾기 문제의 해답
def solution(num_list: list, n: int) -> int:
    """정수 리스트에 주어진 정수 n이 있는지 확인합니다.

    Args:
        num_list (list[int]): 주어진 정수 리스트.
        n (int): 확인 정수.

    Returns:
        int: 정수 n이 있다면 1, 없다면 0을 반환합니다.
    """
    return int(n in num_list)

print(solution([1, 2, 3, 4, 5], 3))       # 1
print(solution([15, 98, 23, 2, 15], 20))  # 0