# LV0 - 왼쪽 오른쪽
def solution(str_list):
    """
    :param str_list: list
    :return: list
    """
    for i, s in enumerate(str_list):
        if s == "l":
            return str_list[:i]
        elif s == "r":
            return str_list[i + 1:]
    return []

print(solution(["u", "u", "l", "r"]))  # ["u", "u"]
print(solution(["l"]))  # []
