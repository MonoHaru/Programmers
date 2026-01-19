# LV1 - 핸드폰 번호 가리기 문제의 해답
def solution(phone_number):
    """    
    :param phone_number: 전화번호 문자열
    """
    return "*" * len(phone_number[:-4]) + phone_number[-4:]

print("01033334444")  # "*******4444"
print("027778888")  # "*****8888"