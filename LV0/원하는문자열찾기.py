# LV0 - 원하는 문자열 찾기 문제의 해답
def solution(myString, pat):
    """
    :param myString: str
    :param pat: str
    :return: int
    """
    return int(pat.lower() in myString.lower())

print(solution("AbCdEfG", "aBc"))  # 1
print(solution("aaAA", "aaaaa"))  # 0