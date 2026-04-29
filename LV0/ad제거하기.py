# LV0 - ad 제거하기 문제의 해답
def solution(strArr: list) -> list:
    """
    문자열에서 'ad'를 포함하는 문자열을 제거합니다.

    Args:
        strArr (list[str]): 입력 문자열 리스트

    Returns:
        list[str]: 'ad'가 제거된 문자열
    """
    return [str for str in strArr if "ad" not in str]