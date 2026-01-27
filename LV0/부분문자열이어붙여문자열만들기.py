# LV0 - 부분 문자열 이어 붙여 문자열 만들기 문제의 해답
def solution(my_strings, parts):
    """
    :param my_strings: list
    :param parts: list
    :return: str
    """
    return ''.join([word[idx[0]:idx[1]+1] for word, idx in zip(my_strings, parts)])

my_strings = ["progressive", "hamburger", "hammer", "ahocorasick"]
parts = [[0, 4], [1, 2], [3, 5], [7, 7]]
print(solution(my_strings, parts))  # "programmers"