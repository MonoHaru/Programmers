# LV0 - 369게임 문제의 해답
def solution(order: int) -> int:
    """주어진 정수에서 369 개수를 찾습니다.

    Args:
        order (int): 주어진 정수.
    
    Returns:
        int: 369의 갯수.
    """
    answer = 0
    for i in str(order):
        if i in '369':
            answer += 1
    return answer

print(solution(3))      # 1
print(solution(29423))  # 2