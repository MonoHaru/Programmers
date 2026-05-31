# LV0 - 팩토리얼 문제의 해답
def solution(n: int) -> int:
    """n과 같거나 작은 가장 큰 팩토리얼 수를 구합니다.

    Args:
        n (int): 주어진 자연수.

    Returns:
        int: 같거나 가장 큰 팩토리얼.
    """
    answer, fact = 1, 0
    while answer <= n:
        fact += 1
        answer *= fact
        
    return fact - 1

print(solution(3628800))  # 10
print(solution(7))        # 3