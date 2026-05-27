def solution(n: int) -> list:
    """나선형으로 순차적으로 값이 들어있는 이차원 배열을 만듭니다.

    Args:
        n (int): 배열의 크기 n x n.
    
    Returns:
        list: 나선형으로 숫자가 들어있는 이차원 배열.    
    """
    answer = [[0] * n for i in range(n)]
    x, y = 0, 0
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    action = 0
    for i in range(1, n ** 2 + 1):
        answer[x][y] = i
        if (x + dx[action]) >= n or (y + dy[action]) >= n or answer[x + dx[action]][y + dy[action]] != 0:
            action = (action + 1) % 4
        x = x + dx[action]
        y = y + dy[action]
    return answer

print(solution(4))
"""
[[1, 2, 3, 4], 
[12, 13, 14, 5], 
[11, 16, 15, 6], 
[10, 9, 8, 7]]
"""
print(solution(5))
"""
[[1, 2, 3, 4, 5], 
[16, 17, 18, 19, 6],
[15, 24, 25, 20, 7],
[14, 23, 22, 21, 8], 
[13, 12, 11, 10, 9]]
"""