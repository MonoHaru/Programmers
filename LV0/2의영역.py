# LV0 - 2의 영역 문제의 해답
def solution(arr):
    """
    :param arr: list
    :return: list
    """
    if 2 not in arr:
        return [-1]
    return arr[arr.index(2):len(arr) - arr[::-1].index(2)]

print(solution([1, 2, 1, 4, 5, 2, 9]))  # [2, 1, 4, 5, 2]
print(solution([1, 2, 1]))  # [2]
print(solution([1, 1, 1]))  # [-1]
print(solution([1, 2, 1, 2, 1, 10, 2, 1]))  # [2, 1, 2, 1, 10, 2]