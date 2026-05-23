# LV0 - 꼬리 문자열 문제의 해답
def solution(str_list: list, ex: str) -> str:
    """문자열 리스트에 있는 문자열로 새로문 문자열을 만듭니다.

    리스트에 있는 문자열에 부분 문자열 ex가 속하지 않는 문자열만 가지고 새로운 문자열을 만듭니다.
    
    Args:
        str_list (list[str]): 문자열 리스트.
        ex (str): 부분 문자열.

    Returns:
        str: 새로 만들어진 문자열.    
    """
    answer = ''
    for n in str_list:
        if ex not in n:
            answer += n
    return answer

print(solution(["abc", "def", "ghi"], "ef"))  # "abcghi"
print(solution(["abc", "bbc", "cbc"], "c"))   # ""