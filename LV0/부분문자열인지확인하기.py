# LV0 - 부분 문자열인지 확인하기 문제의 해답
def solution(my_string: str, target: str) -> int:
    """문자열 my_string에 target이 있는지 확인합니다.

    Args:
        my_string (str): 전체 문자열.
        target (str): 부분 문자열.

    Returns:
        target이 my_string에 있으면 1,
        없으면 0을 반환합니다.   
    """
    return 1 if target in my_string else 0

print(solution("banana", "ana"))  # 1
print(solution("banana", "wxyz"))  # 0