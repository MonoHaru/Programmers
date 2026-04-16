# LV0 - 특정한 문자를 대문자로 바꾸기 문제의 해답
def solution(my_string, alp):
    """
    :param my_string: str
    :param alp: str
    :return: str
    """
    return my_string.replace(alp, chr(ord(alp) - 32))

print(solution("programmers", "p"))  # "Programmers"
print(solution("lowercase", "x"	))  # "lowercase"