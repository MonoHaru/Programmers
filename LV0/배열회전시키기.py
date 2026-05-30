# LV0 - 배열 회전시키기 문제의 해답
def solution(numbers: list, direction: str) -> list:
    """정수 배열(numbers)를 주어진 방향(direction)으로 회전시킵니다.

    Args:
        numbers (list[int]): 정수 배열.
        direction (str): 회전 방향.

    Returns:
        list[int]: 회전된 정수 배열.
    """
    if direction == "right":
        return [numbers[-1]] + numbers[:-1]
    elif direction == "left":
        return numbers[1:] + [numbers[0]]
    
print(solution([1, 2, 3], "right"))                 # [3, 1, 2]
print(solution([4, 455, 6, 4, -1, 45, 6], "left"))  # [455, 6, 4, -1, 45, 6, 4]