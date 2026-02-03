def solution(s):
    """
    :param s: str
    :return: bool
    """
    return s.isdigit() and len(s) in [4, 6]

print(solution("a234"))  # False
print(solution("1234"))  # True
