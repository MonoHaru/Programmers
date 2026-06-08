# LV0 - 인덱스 바꾸기 문제의 해답
def solution(my_string: str, num1: int, num2: int) -> str:
    """주어진 문자열(my_string)의 num1번째와 num2번째 글자를 바꿉니다.

    Args:
        my_string (str): 주어진 문자열.
        num1 (int): 첫 번째 위치.
        num2 (int): 두 번째 위치.
    
    Returns:
        str: 위치가 바뀐 문자열.    
    """
    answer = list(my_string)
    answer[num1], answer[num2] = answer[num2], answer[num1]        
    return ''.join(answer)

print(solution("hello", 1, 2))       # "hlelo"
print(solution("I love you", 3, 6))  # "I l veoyou"