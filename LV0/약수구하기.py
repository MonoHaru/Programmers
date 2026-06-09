# LV0 - 약수 구하기 문제의 해답
def solution(n: int) -> list:
    """주어진 정수 n의 약수를 오름차순으로 구합니다.

    Args:
        n (int): 주어진 정수.

    Returns:
        list[int]: 정렬된 약수 리스트.    
    """
    return [i for i in range(1, n + 1) if not n % i]

print(solution(24))  # [1, 2, 3, 4, 6, 8, 12, 24]
print(solution(29))  # [1, 29]