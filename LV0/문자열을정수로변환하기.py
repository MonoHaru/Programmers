# LV0 - 문자열을 정수로 변환하기 문제의 해답
def solution(n_str: str) -> int:
    """주어진 문자열 n_str을 숫자로 표현합니다.

    Args:
        n_str (str): 숫자로 이루어진 문자열.

    Returns:
        int: 숫자로 표현되는 문자열 n_str.    
    """
    return int(n_str)

print(solution("10"))  # 10
print(solution("8542"))  # 8542