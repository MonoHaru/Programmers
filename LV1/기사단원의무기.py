# LV1 - 기사단원의 무기 문제의 해답
def solution(number, limit, power):
    """
    :param number: int
    :param limit: int
    :param power: int
    """
    fact_cnt = [0] * (number + 1)

    for i in range(1, number + 1):
        for j in range(i, number + 1, i):
            fact_cnt[j] += 1

    total = 0
    for i in range(1, number + 1):
        if fact_cnt[i] > limit:
            total += power
        else:
            total += fact_cnt[i]
            
    return total

print(solution(5, 3, 2))  # 10
print(solution(10, 3, 2))  # 21