# LV0 - k의 개수 문제의 해답
def solution(i: int, j: int, k: int) -> int:
    """i~j 중 k가 나타나는 횟수를 구합니다.

    Args:
        i (int): 시작 수.
        j (int): 최종 수.
        k (int): 찾을 수.

    Returns:
        int: k가 나타나는 횟수.    
    """
    answer = 0
    for n in range(i, j + 1):
        answer += str(n).count(str(k))
    return answer

print(solution(1, 13, 1))   # 6
print(solution(10, 50, 5))  # 5
print(solution(3, 10, 2))   # 0