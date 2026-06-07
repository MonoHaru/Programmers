# LV0 - 암호 해독 문제의 해답
def solution(cipher: str, code: int) -> str:
    """주어진 암호(cipher)에서 code번째 문자만 가져옵니다.

    Args:
        cipher (str): 주어진 암호 문자열.
        code (int): 암호 해독을 위한 정수.

    Returns:
        str: 해독된 암호.    
    """
    return ''.join(cipher[code-1::code])

print(solution("dfjardstddetckdaccccdegk", 4))  # "attack"
print(solution("pfqallllabwaoclk", 2))          # "fallback"