# LV0 - 중복된 문자 제거 문제의 해답
def solution(my_string: str) -> str:
    """중복되는 문자를 제거합니다.

    Args:
        my_string (str): 주어진 문자열.

    Returns:
        str: 중복이 제거된 문자열.    
    """
    answer = ''
    for c in my_string:
        if c not in answer:
            answer += c
    return answer

print(solution("people"))            # "peol"
print(solution("We are the world"))  # "We arthwold"