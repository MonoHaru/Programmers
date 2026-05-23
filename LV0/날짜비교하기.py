# LV0 - 날짜 비교하기 문제의 해답
def solution(date1: list, date2: list) -> int:
    """두 리스트의 날짜 정보를 비교합니다.

    Args:
        date1 (list[int]): 날짜 정보 리스트 1.
        date2 (list[int]): 날짜 정보 리스트 2.

    Returns:
        int : date1이 더 빠르면 1, date2가 더 빠르면 0을 반환합니다.
    """
    for d1, d2 in zip(date1, date2):
        if d1 < d2:
            return 1
        elif d2 < d1:
            return 0
    return 0

print(solution([2021, 12, 28], [2021, 12, 29]))  # 1
print(solution([1024, 10, 24], [1024, 10, 24]))  # 0