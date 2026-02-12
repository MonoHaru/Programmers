# LV0 - 가까운 1 찾기 문제의 해답
def solution(arr, idx):
    """
    :param arr: list
    :param idx: int
    :return: int
    """
    for i in range(idx, len(arr)):
        if arr[i]:
            return i
    return -1

print(solution([0, 0, 0, 1], 1))  # 3
print(solution([1, 0, 0, 1, 0, 0], 4))  # -1
print(solution([1, 1, 1, 1, 0], 3))  # 3