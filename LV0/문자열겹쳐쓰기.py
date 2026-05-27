# LV0 - 문자열 겹쳐쓰기 문제의 해답
def solution(my_string: str, overwrite_string: str, s: int) -> str:
    """주어진 문자열로 새로운 문자열을 만듭니다.

    my_string의 s번째 인덱스부터 s + len(overwrite_string)까지
    overwrite_string으로 교체합니다.

    Args:
        my_string (str): 주어진 원래 문자열.
        overwrite_string (str): 교체될 문자열.
        s (int): 교체 인덱스.

    Returns:
        str: 새롭게 만들어진 문자열.    
    """
    return my_string[:s] + overwrite_string + my_string[s + len(overwrite_string):] 

print(solution("He11oWor1d", "lloWorl", 2))      # "HelloWorld"
print(solution("Program29b8UYP", "merS123", 7))  # "ProgrammerS123"