# LV0 - 세로 읽기 문제의 해답
def solution(my_string, m, c):
    """
    :param my_string: str
    :param m: int
    :param c: int
    :return: str
    """
    return my_string[c-1::m]

print(solution("ihrhbakrfpndopljhygc", 4, 2))  # "happy"
print(solution("programmers", 1, 1))  # "programmers"