# LV0 - 문자의 뒤의 n글자 문제의 해답
def solution(my_string, n):
    """
    :param my_string: str
    :param n: int
    """
    return my_string[-n:]

print(solution("ProgrammerS123", 11))  # "grammerS123"
print(solution("He110W0r1d", 5))  # "W0r1d"