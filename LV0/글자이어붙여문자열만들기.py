# LV0 - 글자 이어 붙여 문자열 만들기 문제의 해답
def solution(my_string, index_list):
    """
    :param my_string: 문자열
    :param index_list: 정수 배열
    """
    return ''.join([my_string[i] for i in index_list])

print(solution("cvsgiorszzzmrpaqpe", [16, 6, 5, 3, 12, 14, 11, 11, 17, 12, 7]))  # "programmers"
print(solution("zpiaz", [1, 2, 0, 0, 3]))  # "pizza"