# LV1 - 콜라 문제의 해답
def solution(a, b, n):
    """
    :param a: int
    :param b: int
    :param n: int
    :return: int
    """
    drink = 0
    while n >= a:
        coke, empty = (n // a) * b, n % a
        drink += coke
        n = coke + empty
    return drink

print(solution(2. 1, 20))  # 19
print(solution(3, 1, 20))  # 9