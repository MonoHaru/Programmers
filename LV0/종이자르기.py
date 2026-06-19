# LV0 - 종이 자르기 문제의 해답
def solution(M: int, N: int) -> int:
    """M x N 크기 종이를 1 x 1 크기로 몇 개 자를 수 있을 지 찾습니다.

    Args:
        M (int): 가로 길이.
        N (int): 세로 길이.
    
    Returns:
        int: 자를 수 있는 개수.    
    """
    return N * M - 1

print(solution(2, 2))  # 3
print(solution(2, 5))  # 9
print(solution(1, 1))  # 0