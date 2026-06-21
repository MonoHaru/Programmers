# LV0 - 치킨 쿠폰 문제의 해답
def solution(chicken: int) -> int:
    """치킨 쿠폰을 먹을 수 있는 치킨의 개수를 구합니다.

    쿠폰 10개로 하나를 시켜먹을 수 있습니다.

    Args:
        chicken (int): 이제껏 시켜먹은 치킨 수.

    Returns:
        int: 쿠폰으로 먹을 수 있는 치킨의 최대 개수.    
    """
    answer = 0
    while chicken >= 10:
        quot, rema = divmod(chicken, 10)
        
        answer += quot
        chicken = quot + rema
        
    return answer

print(solution(100))   # 11
print(solution(1081))  # 120