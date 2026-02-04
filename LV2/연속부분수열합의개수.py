# LV2 - 연속 부분 수열 합의 개수 문제의 해답
def solution(elements):
    """
    :param elements: list
    :return: int
    """
    len_e = len(elements)
    total = set()
    for i in range(len_e):
        total.add(elements[i])
        for j in range(1, len_e):
            if i + j <= len_e:
                total.add(sum(elements[i:i+j]))
            else:
                total.add(sum(elements[i:] + elements[:(i+j) % len_e]))
    total.add(sum(elements))
    return len(total)

print(solution([7, 9, 1, 1, 4]))  # 18