# LV0 - 숫자 찾기 문제의 해답
def solution(num: int, k: int) -> int:
    """주어진 정수 num 안에 k가 가장 처음 나타나는 위치를 찾습니다.

    Args:
        num (int): 주어진 정수.
        k (int): 찾을 정수.

    Returns:
        int: 나타난 위치.    
    """
    if str(k) in str(num):
        return str(num).index(str(k)) + 1
    return -1

print(solution(29183, 1))   # 3
print(solution(232443, 4))  # 4
print(solution(123456, 7))  # -1 