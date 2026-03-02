# LV2 - 게임 맵 최단거리 문제의 해답
def solution(maps):
    """
    :param maps: list
    :return : int
    """
    n, m = len(maps), len(maps[0])
    dist = [[0] * m for _ in range(n)]
    dist[0][0] = 1
    from collections import deque
    q = deque([(0, 0)])
    
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
    while q:
        x, y = q.popleft()
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n:
                if maps[ny][nx] == 1 and dist[ny][nx] == 0:
                    dist[ny][nx] = dist[y][x] + 1
                    if ny == n - 1 and nx == m - 1:
                        return dist[ny][nx]
                    q.append((nx, ny))
    return -1

print(solution(
    [[1,0,1,1,1],
     [1,0,1,0,1],
     [1,0,1,1,1],
     [1,1,1,0,1],
     [0,0,0,0,1]]))  # 11
print(solution(
    [[1,0,1,1,1],
     [1,0,1,0,1],
     [1,0,1,1,1],
     [1,1,1,0,0],
     [0,0,0,0,1]]))  # -1