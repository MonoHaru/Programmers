# LV0 - 세 개의 구분자 문제의 해답
def solution(myStr: str) -> list:
    """
    myStr에서 'a', 'b', 그리고 'c' 기준으로 분할한 결과를 반환합니다.
    분할 결과가 비어 있는 경우 ['EMPTY']를 반환합니다.

    Args:
        myStr (str): 입력 문자열.

    Returns:
        list: 분할된 문자열 리스트 또는 ['EMPTY'].
    
    """
    import re
    myStr = [x for x in re.split('[abc]', myStr) if x] 
    if myStr:
        return myStr
    else:
        return ['EMPTY']
    
print(solution("baconlettucetomato"))  # ["onlettu", "etom", "to"]
print(solution("abcd"))  # ["d"]
print(solution("cabab"))  # ["EMPTY"]