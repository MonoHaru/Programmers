# LV0 - 문자열 바꿔서 찾기 문제의 해답
def solution(
    myString: str, 
    pat: str,
) -> int:
    """
    myString에서 "A"와 "B"를 서로 바꾼 뒤,
    해당 문자열 안에 pat이 포함되어 있는지 확인합니다.

    Args:
        myString (str): 'A'와 'B'를 바꿀 대상 문자열.
        pat (str): 포함 여부를 확인할 문자열.

    Returns:
        int: pat이 존재하면 1, 아니면 0.
    """
    answer = ''
    for ch in myString:
        if ch == 'A':
            answer += 'B'
        elif ch == 'B':
            answer += 'A'
    return int(pat in answer)

print(solution("ABBAA", "AABB"))  # 1
print(solution("ABAB", "ABAB"))  # 0