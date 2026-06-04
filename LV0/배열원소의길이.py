# LV0 - 배열 원소의 길이 문제의 해답
def solution(strlist: list) -> list:
    """주어진 배열의 문자열 원소 길이를 반환합니다.

    Args:
        strlist (list[str]): 문자열 배열.

    Returns:
        list[int]: 길이 배열.    
    """
    return [len(word) for word in strlist]

print(solution(["We", "are", "the", "world!"]))  # [2, 3, 3, 6]
print(solution(["I", "Love", "Programmers."]))   # [1, 4, 12]