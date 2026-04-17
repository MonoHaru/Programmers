# LV0 - 특정 문자열로 끝나는 가장 긴 부분 문자열 찾기 문제의 해답
def solution(myString, pat):
    """
    :param myString: str
    :param pat: str
    :return: str
    """
    return myString[:myString.rfind(pat)+len(pat)] 

print(solution("AbCdEFG", "dE"))  # "AbCdE"
print(solution("AAAAaaaa", "a"))  # "AAAAaaaa"