# LV1 - 문자열 내림차순으로 배치하기 문제의 해답
def solution(s):
    """
    :param s: str
    :return: str
    """
    return ''.join(sorted(s, reverse=True))

print(solution("Zbcdefg"))  # "gfedcbZ"