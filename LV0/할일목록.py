# LV0 - 할 일 목록 문제의 해답
def solution(todo_list, finished):
    """
    :param todo_list: list
    :param finished: list
    :return: list
    """
    return [x for x, y in zip(todo_list, finished) if not y]

print(solution(["problemsolving", 
                "practiceguitar", 
                "swim", 
                "studygraph"],
                [True, False, True, False]))  # ["practiceguitar", "studygraph"]