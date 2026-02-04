# LV0 - 문자열 뒤집기 문제의 해답
def solution(my_string, s, e):
    """
    :param my_string: str
    :param s: int
    :param e: int
    :return: str
    """
    return my_string[:s] + my_string[s:e+1][::-1] + my_string[e+1:]

print(solution("Progra21Sremm3", 6, 12))  # "ProgrammerS123"
print(solution("Stanley1yelnatS", 4, 10))  # "Stanley1yelnatS"