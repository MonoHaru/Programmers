# LV0 - 편지 문제의 해답
def solution(message: str) -> int:
    """편지 길이의 2배를 구합니다.

    Args:
        message (str): 편지 문자열.

    Returns:
        int: 편지 길이의 2배.    
    """
    return len(message) * 2

print(solution("happy birthday!"))  # 30
print(solution("I love you~"))      # 22