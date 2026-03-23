# LV0 - 수열과 구간 쿼리 1 문제의 해답
def solution(arr, queries):
    """
    :param arr: list
    :param queries: list
    :return: list
    """
    for s, e in queries:
        for i in range(s, e+1):
            arr[i] += 1
    return arr

print(solution([0, 1, 2, 3, 4],
               [[0, 1],[1, 2],[2, 3]]))  # [1, 3, 4, 4, 4]