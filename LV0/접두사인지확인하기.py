# LV0 - 접두사인지 확인하기 문제의 해답
def solution(my_string, is_prefix):
    """
    :param my_string: str
    :param is_prefix: str
    :return: int
    """
    return int(my_string[:len(is_prefix)] == is_prefix)

print(solution("banana", "ban"))  # 1
print(solution("banana", "nan"))  # 0
print(solution("banana", "abcd"))  # 0
print(solution("banana", "bananan"))  # 0