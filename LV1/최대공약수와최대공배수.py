# LV1- 최대공약수와 최소공배수 문제의 해답
def gcd(a, b):
    """
    :param a: int
    :param b: int
    :return: int
    """
    return b if a % b == 0 else gcd(b, a % b)

def lcm(a, b, gcd_):
    """
    :param a: int
    :param b: int
    :param gcd_: int
    :return: int
    """
    return a // gcd_ * b

def solution(n, m):
    """
    :param n: int
    :param m: int
    :return: list
    """
    gcd_ = gcd(n, m)
    lcm_ = lcm(n, m, gcd_)
    return [gcd_, lcm_]

print(solution(3, 12))  # [3, 12]
print(solution(2, 5))  # [1, 10]