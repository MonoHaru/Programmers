# LV0 - 모음 제거 문제의 해답
def solution(my_string: str) -> str:
    """주어진 문자열에서 모음을 제거합니다.

    Args:
        my_string (str): 주어진 문자열.

    Returns:
        str: 모음이 제거된 문자열.
    """
    answer = ''
    for c in my_string:
        if c in "aeiou":
            continue
        answer += c
    return answer

print(solution("bus"))               # "bs"
print(solution("nice to meet you"))  # "nc t mt y"