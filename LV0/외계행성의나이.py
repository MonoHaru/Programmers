# LV0 - 외계행성의 나이 문제의 해답
def solution(age: int) -> str:
    """정수 나이(age)를 문자로 표현합니다.

    Args:
        age (int): 정수 나이.

    Returns:
        str: 문자 나이.    
    """
    convert = {
        '0': 'a', '1': 'b', '2': 'c', '3': 'd',
        '4': 'e', '5': 'f', '6': 'g', '7': 'h',
        '8': 'i', '9': 'j'
    }
    return ''.join([convert[w] for w in str(age)])

print(solution(23))   # "cd"
print(solution(51))	  # "fb"
print(solution(100))  # "baa"