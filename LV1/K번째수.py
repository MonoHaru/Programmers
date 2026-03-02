# LV1 - K번째수 문제의 해답
def solution(array, commands):
    """
    :param array: list
    :commands: list
    :return: list
    """
    return [sorted(array[i-1:j])[k-1] for i, j, k in commands]

print(solution([1, 5, 2, 6, 3, 7, 4],
               [[2, 5, 3], 
                [4, 4, 1], 
                [1, 7, 3]]))  # [5, 6, 3]