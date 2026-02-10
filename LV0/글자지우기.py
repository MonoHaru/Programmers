# LV0 - 글자 지우기 문제의 해답
def solution(my_string, indices):
    """
    :param my_string: str
    :param indices: list
    :return: str
    """
    answer = ''
    for i in range(len(my_string)):
        if i not in indices:
            answer += my_string[i]
    return answer

print(solution("apporoograpemmemprs", 
               [1, 16, 6, 15, 0, 10, 11, 3]))  # "programmers"