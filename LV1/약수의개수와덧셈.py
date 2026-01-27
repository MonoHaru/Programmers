# LV1 - 약수의 개수와 덧셈 문제의 해답
def solution(left, right):
    """
    :param left: int
    :param right: int
    :return: int
    """
    return sum([-i if i**0.5 == int(i**0.5) else i for i in range(left, right + 1)])
    

print(solution(13, 17))  # 43
print(solution(24, 27))  # 52