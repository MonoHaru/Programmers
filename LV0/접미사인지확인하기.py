# LV0 - 접미사인지 확인하기 문제의 해답
def solution(my_string, is_suffix):
    """
    :param my_string: str
    :param is_suffix: str
    :return: str
    """
    return 1 if my_string[-len(is_suffix):] == is_suffix else 0

print(solution("banana", "ana"))  # 1
print(solution("banana", "nan"))  # 0
print(solution("banana", "wxyz"))  # 0
print(solution("banana", "abanana"))  # 0 