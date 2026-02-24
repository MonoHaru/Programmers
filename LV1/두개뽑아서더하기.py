# LV1 - 두 개 뽑아서 더하기 문제의 해답
def solution(numbers):
    """
    :param numbers: list
    :return: list
    """
    ans = set()
    from itertools import combinations
    for cb in combinations(numbers, 2):
        ans.add(sum(cb))
    return sorted(list(ans))

print(solution([2,1,3,4,1]))  # [2,3,4,5,6,7]
print(solution([5,0,2,7]))  # [2,5,7,9,12]