# LV0 - 저주의 숫자 3 문제의 해답
def solution(n: int) -> int:
    """3의 배수와 3이 들어간 숫자를 뛰어넘어 주어진 n의 수를 구합니다.

    Args:
        n (int): 주어진 수.

    Returns:
        int: 3의 배수 혹은 3을 포함한 수를 건너뛴 수.
    """
    answer = 0
    for _ in range(n):
        answer += 1
        while '3' in str(answer) or answer % 3 == 0:
            answer += 1
    return answer

print(solution(15))  # 25
print(solution(40))  # 76