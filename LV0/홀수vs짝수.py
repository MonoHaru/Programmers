# LV0 - 홀수 vs 짝수 문제의 해답
def solution(num_list):
    """
    :param num_list: list
    :return: int
    """
    return max(sum(num_list[0::2]), sum(num_list[1::2]))

print(solution([4, 2, 6, 1, 7, 6]))  # 17
print(solution([-1, 2, 5, 6, 3]))  # 8