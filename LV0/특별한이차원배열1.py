# LV0 - 특별한 이차원 배열 1 문제의 해답
def solution(n: int) -> list:
    """크기 n의 단위 행렬을 만듭니다.

    Args:
        n (int): 단위 행렬 행과 열의 크기.

    Returns:
        list: 크기 n의 단위 행렬.    
    """
    answer = []
    for i in range(n):
        sub = []
        for j in range(n):
            if i == j:
                sub.append(1)
            else:
                sub.append(0)
        answer.append(sub)
    return answer

print(solution(3))  # [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
print(solution(6))
"""
[[1, 0, 0, 0, 0, 0], 
[0, 1, 0, 0, 0, 0], 
[0, 0, 1, 0, 0, 0], 
[0, 0, 0, 1, 0, 0], 
[0, 0, 0, 0, 1, 0], 
[0, 0, 0, 0, 0, 1]]
"""
print(solution(1))  # [[1]]