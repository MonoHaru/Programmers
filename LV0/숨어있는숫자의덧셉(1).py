# LV0 - 숨어있는 숫자의 덧셈 (1) 문제의 해답
def solution(my_string):
    """주어진 문자열에 있는 숫자의 총합을 구합니다.

    Args:
        my_string (str): 주어진 문자열.

    Returns:
        int: 숫자의 총합.    
    """
    answer = 0
    for w in my_string:
        if w.isdigit():
            answer += int(w)
    return answer

print(solution("aAb1B2cC34oOp"))  # 10
print(solution("1a2b3c4d123"))    # 16