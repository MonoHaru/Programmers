# LV0 - 문자열안에 문자열 문제의 해답
def solution(str1: str, str2: str) -> int:
    """주어진 문자열 str1안에 str2가 있는지 확인합니다.

    Args:
        str1 (str): 주어진 문자열 1.
        str2 (str): 주어진 문자열 2.

    Returns:
        int: 있으면 1, 없으면 2를 반환합니다.    
    """
    return 1 if str2 in str1 else 2

print(solution("ab6CDE443fgh22iJKlmn1o", "6CD"))  # 1
print(solution("ppprrrogrammers", "pppp"))        # 2
print(solution("AbcAbcA", "AAA"))                 # 2