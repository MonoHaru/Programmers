# LV0 - 문자열 잘라서 정렬하기 문제의 해답
def solution(myString: str) -> list:
    """
    x로 분할된 리스트를 정렬합니다.

    Args:
        myString (str): 입력 문자열.
    
    Returns:
        x를 기준으로 분해된 리스트를 정렬한 리스트.

    """
    myString = [x for x in myString.split('x') if x]
    return sorted(myString)

print(solution("axbxcxdx"))  # ["a","b","c","d"]
print(solution("dxccxbbbxaaaa"))  ["aaaa","bbb","cc","d"]