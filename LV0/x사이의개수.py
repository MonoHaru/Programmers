def solution(myString):
    """
    x로 분할된 리스트의 길이로 배열을 만듭니다.

    Args:
        myString (str): 입력 문자열.
    
    Returns:
        x를 기준으로 분해된 리스트의 길이 정보로 구성된 배열.
    """
    return [len(x) for x in myString.split('x')]

print(solution("oxooxoxxox"))  # [1, 2, 1, 0, 1, 0]
print(solution("xabcxdefxghi"))  # [0, 3, 3, 3]