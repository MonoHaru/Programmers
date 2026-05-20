# LV0 - 두 수의 합 문제의 해답
def solution(a: str, b: str) -> str:
    """주어진 문자열 a와 b의 합을 구합니다.
    
    이때, 문자열로 반환합니다.

    Args:
        a (str): 숫자로 이루어진 문자열.
        b (str): 숫자로 이루어진 문자열.

    Returns:
        str: a와 b의 합을 문자열로 반환.
    
    """
    return str(int(a) + int(b))

print(solution("582", "734"))  # "1316"
print(solution("18446744073709551615", "287346502836570928366"))  # "305793246910280479981"
print(solution("0", "0"))  # "0"