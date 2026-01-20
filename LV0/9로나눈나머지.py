# LV0 - 9로 나눈 나머지
def solution(number):
    """
    :param number: str -> 숫자 문자열
    """
    return sum([int(n) for n in list(number)]) % 9

print(solution("123"))  # 6
print(solution("78720646226947352489"))  # 2