# LV0 - 자릿수 더하기 문제의 해답
def solution(n: int) -> int:
    """숫자 n 각 자릿수 합을 구합니다.

    Args:
        n (int): 주어진 정수.

    Returns:
        int: 각 자릿수의 합.    
    """
    return sum(list(map(int, str(n))))

print(solution(1234))    # 10
print(solution(930211))  # 16