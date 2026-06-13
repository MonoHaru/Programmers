# LV0 - 캐릭터의 좌표 문제의 해답
def solution(keyinput: list, board: list) -> list:
    """모든 행동 후 최종 좌표를 구합니다.

    Args:
        keyinput (list[str]): 움직임 키워드.
        board (list[int]): 보드 전체 크기.

    Returns:
        list[int]: 최종 좌표.    
    """
    move = {
        'left': [-1, 0],
        'right': [1, 0],
        'up': [0, 1],
        'down': [0, -1]
    }
    point = [0, 0]
    max_x, max_y = board[0] // 2, board[1] // 2
    for k in keyinput:
        dx, dy = move[k]
        if abs(point[0] + dx) > max_x or abs(point[1] + dy) > max_y:
            continue
        point[0] += dx
        point[1] += dy
    return point

print(solution(["left", "right", "up", "right", "right"], [11, 11]))  # [2, 1]
print(solution(["down", "down", "down", "down", "down"], [7, 9]))     # [0, -4]