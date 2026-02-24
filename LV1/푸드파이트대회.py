# LV1 - 푸드 파이트 대회 문제의 해답
def solution(food):
    """
    :param food: list
    :return: str
    """
    ans = ''
    for i, cal in enumerate(food):
        cnt = cal // 2
        if cnt != 0:
            ans += str(i) * cnt
    return ans + '0' + ans[::-1]

print(solution([1, 3, 4, 6]))  # "1223330333221"
print(solution([1, 7, 1, 2]))  # "111303111"