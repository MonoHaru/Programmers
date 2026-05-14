# LV0 - 뒤에서 5등 위로 문제의 해답
def solution(num_list: list) -> list:
    """
    Args:
        num_list (list): ...

    Returns:
        list: ...
    """
    return sorted(num_list)[5:]

print(solution([12, 4, 15, 46, 38, 1, 14, 56, 32, 10]))  # [15, 32, 38, 46, 56]