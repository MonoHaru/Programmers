# LV0 - rny_string 문제의 해답
def solution(rny_string: str) -> str:
    """
    rny_string에서 'm'을 'rn'으로 교체한 문자열을 반환합니다.

    Args:
        rny_string (str): 입력 문자열.

    Returns:
        str: 교체된 문자열.
    """
    return rny_string.replace('m', 'rn')

print(solution("masterpiece"))  # "rnasterpiece"
print(solution("programmers"))  # "prograrnrners"
print(solution("jerry"))  # "jerry"
print(solution("burn"))  # "burn"