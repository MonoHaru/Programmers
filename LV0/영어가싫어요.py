# LV0 - 영어가 싫어요 문제의 해답
def solution(numbers: str) -> int:
    """숫자가 표현된 주어진 문자열(numbers)을 정수형으로 변환합니다.

    Args:
        numbers (str): 숫자가 표현된 문자열.

    Returns:
        int: 숫자로 표현된 정수.    
    """
    dic_n = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    for k, v in dic_n.items():
        numbers = numbers.replace(k, v)
    return int(numbers)


print(solution("onetwothreefourfivesixseveneightnine"))  # 123456789
print(solution("onefourzerosixseven"))  # 14067