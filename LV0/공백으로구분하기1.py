# LV0 - 공백으로 구분하기 1 문제의 해답
def solution(my_string: str) -> list:
    """
    문자열에서 띄어쓰기 기준으로 나누어 문자열 리스트 만듭니다.

    Args:
        my_string (str): 입력 문자열.

    Returns:
        띄어쓰기 기준으로 나누어진 문자열 리스트.
    """
    return my_string.split()

print(solution("i love you"))  # ["i", "love", "you"]
print(solution("programmers"))  # ["programmers"]