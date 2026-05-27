# LV0 - 이차원 배열 대각선 순회하기 문제의 해답
def solution(board: list, k: int) -> int:
    """board의 행과 열 합이 k보다 작은 원소의 총합을 구합니다.

    Args:
        board (list[int]): 이차원 정수 배열.

    Returns:
        k보다 작은 행과 열 합 원소의 총합.    
    """
    answer = 0
    m, n = len(board), len(board[0])
    for i in range(m):
        for j in range(n):
            if i + j <= k:
                answer += board[i][j]
    return answer

print(solution([[0, 1, 2],[1, 2, 3],[2, 3, 4],[3, 4, 5]], 2)) # 8