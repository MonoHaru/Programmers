# LV0 - 개미 군단 문제의 헤답
def solution(hp: int) -> int:
    """최소한의 병력 수로 hp를 0으로 만듭니다.

    Args:
        hp (int): 사냥감의 HP.

    Returns:
        int: 병력 수    
    """
    n_5 = hp // 5
    hp = hp - (n_5 * 5)
    
    n_3 = hp // 3
    hp = hp - (n_3 * 3)
        
    return n_5 + n_3 + hp

print(solution(23))   # 5
print(solution(24))   # 6
print(solution(999))  # 201