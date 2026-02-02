# LV! - 부족한 금액 계산하기 문제의 해답
def solution(price, money, count):
    """
    :param price: int
    :param money: int
    :param count: int
    :return: int
    """
    return abs(min(money - sum([price * i for i in range(1, count + 1)]), 0))

print(solution(3, 20, 4))  # 10