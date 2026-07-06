# LV1 - 2016년 문제의 해답
def solution(a: int, b: int) -> str:
    """2016년의 a월 b일이 무슨 요일인지 맞추시오.
    
    Args:
        a (int): 월.
        b (int): 일
    
    Returns:
        str: 요일.
    """
    months = {
        1: 31, 2: 29, 3: 31, 4: 30,
        5: 31, 6: 30, 7: 31, 8: 31,
        9: 30, 10: 31, 11: 30, 12: 31
    }
    days = {
        0: 'FRI', 1: 'SAT', 2: 'SUN', 3: 'MON',
        4: 'TUE', 5: 'WED', 6: 'THU'
    }
    answer = 0
    for i in range(a - 1):
        answer += months[i + 1]
    answer += b

    return days[(answer - 1) % 7]

print(solution(5, 24))  # "TUE"