# LV2 - 행렬의 곱셈 문제의 해답
def solution(arr1, arr2):
    """
    :param arr1: list
    :param arr2: list
    :return: list
    """
    answer = []
    for i in range(len(arr1)):
        arr1_row = arr1[i]
        answer.append([])
        for arr2_col in zip(*arr2):
            sub_answer = 0
            for a, b in zip(arr1_row, arr2_col):
                sub_answer += a * b
            answer[i].append(sub_answer)
    return answer

arr1 = [[1, 4], [3, 2], [4, 1]]
arr2 = [[3, 3], [3, 3]]
print(solution(arr1, arr2))
# [[15, 15], [15, 15], [15, 15]]

arr1 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
arr2 = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]
print(solution(arr1, arr2))
# [[22, 22, 11], [36, 28, 18], [29, 20, 14]]
