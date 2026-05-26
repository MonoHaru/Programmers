# LV0 - 특별한 이차원 배열 2 문제의 해답
def solution(arr: list) -> int:
    """대각 행렬인지 아닌지 확인합니다.

    Args:
        arr (list[int]): 주어진 이차원 배열.

    Returns:
        int: 대각 행렬이면 1, 아니면 0을 반환합니다.    
    """
    lens = len(arr)
    for i in range(len(arr)):
        for j in range(i + 1):
            if i == j:
                continue
            if arr[i][j] != arr[j][i]:
                return 0
    return 1

print(solution([[5, 192, 33], 
                [192, 72, 95], 
                [33, 95, 999]]))  # 1
print(solution([[19, 498, 258, 587], 
                [63, 93, 7, 754], 
                [258, 7, 1000, 723], 
                [587, 754, 723, 81]]))  # 0