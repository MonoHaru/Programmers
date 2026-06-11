# LV0 - A로 B 만들기 문제의 해답
def solution(before: str, after: str) -> int:
    """before로 after를 만들 수 있는지 확인합니다.

    Args:
        before (str): 문자열 1.
        after (str): 문자열 2.

    Returns:
        int: 만들 수 있으면 1, 아니면 0.    
    """
    return 1 if sorted(before) == sorted(after) else 0

print(solution("olleh", "hello"))  # 1
print(solution("allpe", "apple"))  # 0