# LV0 - 문자열 정렬하기 (2) 문제의 해답
def solution(my_string: str) -> str:
    """주어진 문자열을 소문자로 정렬합니다.

    Args:
        my_string (str): 주어진 문자열.

    Returns:
        str: 소문자로 정렬된 문자열.    
    """
    return ''.join(sorted(my_string.lower()))

print(solution("Bcad"))    # "abcd"
print(solution("heLLo"))   # "ehllo"
print(solution("Python"))  # "hnopty"