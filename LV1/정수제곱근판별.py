# LV1 - 정수 제곱근 판별 문제의 해답
def solution(n):
    sqrt_n = n ** (1 / 2)
    return (sqrt_n + 1) ** 2 if sqrt_n.is_integer() else -1
