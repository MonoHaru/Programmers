# LV0 - 유한소수 판별하기
import math

def solution(a: int, b: int) -> int:
    """a/b가 유리수인지 판별합니다.

    Args:
        a (int): 분자 수.
        b (int): 분모 수.
    
    Returns:
        int: 유리수면 1, 무리수면 2를 반환합니다.    
    """
    gcd_value = math.gcd(a, b)
    b //= gcd_value
    
    while b % 2 == 0:
        b //= 2
        
    while b % 5 == 0:
        b //= 5
        
    return 1 if b == 1 else 2

print(solution(7, 20))   # 1
print(solution(11, 22))  # 1
print(solution(12, 21))  # 2