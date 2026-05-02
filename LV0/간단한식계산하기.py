# LV0 - 간단한 식 계산하기 문제의 해답
def solution(binomial: str) -> int:
    """
    간단한 식을 계산합니다.

    Args:
        binomial (str): 입력 문자열.
    
    Returns:
        int: 문자열 계산식 결과. 
    """
    a, op, b = binomial.split(' ')
    
    a, b = int(a), int(b)
    
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    
print(solution("43 + 12"))  # 55
print(solution("0 - 7777"))  # -7777
print(solution("40000 * 40000"))  # 1600000000