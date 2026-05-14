# LV 0 - 뒤에서 5등까지 문제의 해답
def solution(num_list: list) -> list:
    """
    Args:
        num_list (list): ...
    Returns:
        list: ...
    """
    return sorted(num_list)[:5]

print(solution([12, 4, 15, 46, 38, 1, 14]))  # [1, 4, 12, 14, 15]