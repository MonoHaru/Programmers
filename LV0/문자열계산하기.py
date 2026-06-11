# LV0 - 문자열 계산하기 문제의 해답
def solution(my_string: str) -> int:
    """주어진 문자열 수식을 계산합니다.

    Args:
        my_string (str): 주어진 문자열 수식

    Returns:
        int: 수식의 결과.
    """
    return eval(my_string)

print(solution("3 + 4"))  # 7