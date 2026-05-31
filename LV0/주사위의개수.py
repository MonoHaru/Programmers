# LV0 - 주사위의 개수 문제의 해답
def solution(box: list, n: int) -> int:
    """ 크기 n의 주사위가 박스(box)에 몇 개가 들어가지는 계산합니다.

    Args:
        box (list[int]): 박스 크기.
        n (int): 주사위 크기.
    
    Returns:
        int: 박스에 들어가는 주사위 개수.
    """
    x = box[0] // n
    y = box[2] // n
    z = box[2] // n
    return x * y * z

print(solution([1, 1, 1], 1))   # 1
print(solution([10, 8, 6], 3))  # 12