# LV1 - 명예의 전당 (1) 문제의 해답
def solution(k, score):
    """
    :param k: int
    :param score: list
    :return: list
    """
    fame = []
    answer = []
    for s in score:
        fame.append(s)
        if len(fame) > k:
            fame.remove(min(fame))
        answer.append(min(fame))
    return answer

print(solution(3, [10, 100, 20, 150, 1, 100, 200]))
# [10, 10, 10, 20, 20, 100, 100]
print(solution(4, [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]))
# [0, 0, 0, 0, 20, 40, 70, 70, 150, 300]