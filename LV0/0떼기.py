# LV0 - 0 떼기 문제의 해답
def solution(n_str: str) -> str:
    """주어진 문자열 n_str 왼쪽부터 0을 제거합니다.

    Args:
        n_str (str): 숫자로 이루어진 문자열.
        
    Returns:
        str: 왼쪽부터 모든 0이 제거된 문자열.
    
    """
    return n_str.lstrip('0')

print(solution("0010"))  # "10"
print(solution("854020"))  # "854020"