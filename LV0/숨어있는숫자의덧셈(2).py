# LV0 - 숨어있는 숫자의 덧셈 (2) 문제의 해답
def solution(my_string: str) -> int:
    """주어진 문자열 my_string에 있는 숫자의 총합을 구합니다.

    이어진 숫자는 하나의 수로 봅니다.

    Args:
        my_string (str): 주어진 문자열.

    Returns:
        int: 수의 총합.
    """
    answer, temp = 0, ''
    for w in my_string:
        if w.isdigit():
            temp += w
        elif temp:
            answer += int(temp)
            temp = ''           
    return answer + int(temp) if temp else answer

print(solution("aAb1B2cC34oOp"))  # 37
print(solution("1a2b3c4d123Z"))   # 133