# LV1 - 행렬의 덧셈 문제의 해답
def solution(arr1, arr2):
    """
    :param arr1: 2D list
    :param arr2: 2D list
    :return: 2D list
    """
    return [[c + d for c, d in zip(a, b)] for a, b in zip(arr1, arr2)]


arr1 = [[1,2],[2,3]]
arr2 = [[3,4],[5,6]]
print(solution(arr1, arr2))  # [[4,6],[7,9]]

arr1 = [[1],[2]]
arr2 = [[3],[4]]
print(solution(arr1, arr2))  # [[4],[6]]