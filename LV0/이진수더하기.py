# LV0 - 이진수 더하기 문제의 해답
def solution(bin1: str, bin2: str) -> str:
    """두 이진수의 합을 구합니다.

    Args:
        bin1 (str): 이진수 1.
        bin2 (str): 이진수 2.

    Returns:
        str: 두 이진수의 합.    
    """
    return bin(int(bin1, 2) + int(bin2, 2))[2:]

print(solution("10", "11"))      # "101"
print(solution("1001", "1111"))  # "11000"