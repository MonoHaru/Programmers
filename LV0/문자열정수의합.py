# LV0 - 문자열 정수의 합 문제의 해답
def solution(num_str: str) -> int:
    """문자열 num_str에서 각 자리에 있는 값의 합을 구합니다.

    Args:
        num_str (str): 숫자로 이루어진 문자열.

    Returns:
        int: num_str의 각 숫자의 총합    
    """
    return sum(int(n) for n in num_str)

print(solution("123456789"))  # 45
print(solution("1000000"))  # 1