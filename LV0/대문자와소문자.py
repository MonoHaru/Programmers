# LV0 - 대문자와 소문자 문제의 해답
def solution(my_string: str) -> str:
    """주어진 문자열의 대문자와 소문자를 바꿉니다.

    Args:
        my_string (str): 주어진 문자열.
    
    Returns:
        str: 대문자와 소문자가 바뀐 문자열.
    """
    return my_string.swapcase()

print(solution("cccCCC"))      # "CCCccc"
print(solution("abCdEfghIJ"))  # "ABcDeFGHij"