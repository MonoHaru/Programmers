# LV2 - n^2 배열 자르기 문제의 해답
def solution(n, left, right):
    """
    :param n: int
    :param left: int
    :param right: int
    :return: list
    """
    arr = []
    for i in range(left, right+1):
        share = i // n
        remain = i % n
        if share > remain:
            arr.append(share + 1)
        else:
            arr.append(remain + 1)
    return arr

print(solution(3, 2, 5))  # [3, 2, 2, 3]
print(solution(4, 7, 14))  # [4, 3, 3, 3, 4, 4, 4, 4]