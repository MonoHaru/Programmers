# LV1 - 3진법 뒤지기 문제의 해답
def solution(n):
    """
    :param n: int
    :return: int
    """
    answer = ''
    while n > 0:
        n, mod = n // 3, n % 3
        answer += str(mod)
    return int(answer, 3)

print(solution(45))  # 7
print(solution(125))  # 229