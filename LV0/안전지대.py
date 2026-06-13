# LV0 - 안전 지대 문제의 해답
def solution(board: list) -> int:
    """위험 지대가 아닌 그리드 개수를 셉니다.

    1은 지뢰를 나타내며, 주변 그리드를 포함해 모두 위험 지대 입니다.

    Args:
        board (list[int]): 2차원 정수 배열.

    Returns:    
        int: 안전 지대 개수.
    """
    area = [
        [-1, -1], [0, -1], [1, -1],
        [-1, 0],  [0, 0],  [1, 0],
        [-1, 1],  [0, 1],  [1, 1]
    ]
    len_b = len(board)
    answer = [[0] * len_b for i in range(len_b)]
    for i in range(len_b):
        for j in range(len_b):
            if board[i][j]:
                for dx, dy in area:
                    if dx + i < 0 or dx + i >= len_b  or dy + j < 0 or dy + j >= len_b:
                        continue
                    answer[dx + i][dy + j] = 1
    return len_b ** 2 - sum([sum(ans) for ans in answer])


print(solution([
    [0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0], 
    [0, 0, 1, 0, 0], 
    [0, 0, 0, 0, 0]]))  # 16
print(solution([
    [0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0], 
    [0, 0, 1, 1, 0], 
    [0, 0, 0, 0, 0]]))  # 13
print(solution([
    [1, 1, 1, 1, 1, 1], 
    [1, 1, 1, 1, 1, 1], 
    [1, 1, 1, 1, 1, 1], 
    [1, 1, 1, 1, 1, 1], 
    [1, 1, 1, 1, 1, 1], 
    [1, 1, 1, 1, 1, 1]]))  # 0