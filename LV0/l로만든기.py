# LV0 - l로 만들기 문제의 해답
def solution(myString: str) -> str:
    """주어진 문자열에서 l이전 알파벳을 모두 l로 만듭니다.

    Args:
        myString (str): 주어진 문자열.

    Returns:
        str: 반환된 문자열.    
    """
    return ''.join(map(lambda x: x if x > 'l' else 'l', myString))

print(solution("abcdevwxyz"))  # "lllllvwxyz"
print(solution("jjnnllkkmm"))  # "llnnllllmm"