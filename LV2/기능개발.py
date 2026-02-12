# LV2 - 기능개발 문제의 해답
def solution(progresses, speeds):
    """
    :param progresses: list
    :param speeds: list
    :return: list
    """
    due = []
    ans = []
    for prg, spd in zip(progresses, speeds):
        day = get_integer((100 - prg) / spd)
        due.append(day)
        if len(due) == 1:
            continue
        if due[-1] > due[0]:
            ans.append(len(due) - 1)
            due.clear()
            due.append(day)
    ans.append(len(due))
    return ans


def get_integer(n):
    """
    :param n: float
    :return: int
    """
    if n != int(n):
        return int(n) + 1
    return n

print(solution([93, 30, 55], [1, 30, 5]))  # [2, 1]
print(solution([95, 90, 99, 99, 80, 99],
               [1, 1, 1, 1, 1, 1]))  # [1, 3, 2]