# LV0 - 부분 문자열 문제의 해답
def solution(str1: str, str2: str) -> int:
    """전체 문자열 str2에 부분 문자열 str1이 있는지 확인합니다.

    Args:
        str1 (str): 부분 문자열.
        str2 (str): 전체 문자열.

    Returns:
        전체 문자열에 부분 문자열이 있다면 1, 없다면 0을 반환합니다.
    """
    return int(str1 in str2)

print(solution("abc", "aabcc"	))  # 1
print(solution("tbt", "tbbttb"))    # 0