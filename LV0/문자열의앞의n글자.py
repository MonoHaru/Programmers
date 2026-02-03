# LV0 - 문자열의 앞의 n글자 문제의 해답
def solution(my_string, n):
    """
    :param my_string: str
    :param n: int
    :return: str
    """
    return my_string[:n]

print(solution("ProgrammerS123", 11))  # "ProgrammerS"
print(solution("He110W0r1d", 5))  # "He110"