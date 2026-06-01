# LV0 - 문자열 정렬하기 (1) 문제의 해답
def solution(my_string: str) -> list:
    """주어진 문자열에서 숫자를 분리해 정렬합니다.

    Args:
        my_string (str): 주어진 문자열.

    Returns:
        list[int]: 정렬된 리스트.    
    """
    answer = []
    for c in my_string:
        if c.isdigit():
            answer.append(int(c))
    return sorted(answer)

print(solution("hi12392"))    # [1, 2, 2, 3, 9]
print(solution("p2o4i8gj2"))  # [2, 2, 4, 8]
print(solution("abcde0"))     # [0]