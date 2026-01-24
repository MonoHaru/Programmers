# LV0 - 문자열 여러 번 뒤집기
def solution(my_string, queries):
    """
    :param my_string: str
    :param queries: array
    """
    my_string = list(my_string)
    for s, e in queries:
        my_string[s:e+1] = my_string[s:e+1][::-1]
    return ''.join(my_string)

print(solution(
    "rermgorpsam",
    [[2, 3], [0, 7], [5, 9], [6, 10]]
))  # "programmers"