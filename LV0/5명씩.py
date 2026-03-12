# LV0 - 5명씩 문제의 해답
def solution(names):
    """
    :param names: list
    :return: lists
    """
    return names[::5]

print(solution(["nami", 
                "ahri", 
                "jayce", 
                "garen", 
                "ivern", 
                "vex", 
                "jinx"]))  # ["nami", "vex"]