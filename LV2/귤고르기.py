# LV2 - 귤 고르기 문제의 해답
from collections import Counter

def solution(k, tangerine):
    """
    :param k: int
    :param tangerine: list
    :return: int
    """
    counter = sorted(Counter(tangerine).items(), key=lambda x:x[1], reverse=True)
    
    box = 0
    for t, cnt in counter:
        if k > 0:
            k -= cnt
            box += 1
        elif k <= 0:
            break
    return box

print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]))  # 3
print(solution(4, [1, 3, 2, 5, 4, 5, 2, 3]))  # 2
print(solution(2, [1, 1, 1, 1, 2, 2, 2, 3]))  # 1