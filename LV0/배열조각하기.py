# LV0 - 배열 조각하기 문제의 해답
def solution(arr, query):
    """
    :param arr: list
    :param query: list
    :return: list
    """
    for i, q in enumerate(query):
        if i % 2 == 0:
            arr = arr[:q+1]
        else:
            arr = arr[q:]
    return arr

print(solution([0, 1, 2, 3, 4, 5], [4, 1, 2]))  # [1, 2, 3]