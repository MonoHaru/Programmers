# LV0 - 한 번만 등장한 문자 문제의 해답
def solution(s: str) -> str:
    """주어진 문자열에서 한 번만 등장한 문자를 정렬합니다.

    Args:
        s (str): 주어진 문자열.

    Returns:
        str: 한 번만 등장한 정렬된 문자열.    
    """
    stack = []
    for c in s:
        if s.count(c) == 1:
            stack.append(c)
    return ''.join(sorted(stack))

print(solution("abcabcadc"))  # "d"
print(solution("abdc"))       # "abcd"
print(solution("hello"))      # "eho"
