# LV2 - 방문 길이 문제의 해답
def solution(dirs):
    """
    :param dirs: str
    :return: int
    """
    x, y = 0, 0
    actions = {
        "U": (0, 1),
        "D": (0, -1),
        "R": (1, 0),
        "L": (-1, 0),
    }
    states = set()
    for d in dirs:
        nx, ny = x + actions[d][0], y + actions[d][1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            states.add((x, y, nx, ny))
            states.add((nx, ny, x, y))
            x, y = nx, ny
    return len(states) / 2

print(solution("ULURRDLLU"))  # 7
print(solution("LULLLLLLU"))  # 7