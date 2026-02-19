# LV0 - 배열 만들기 3 문제의 해답
def solution(arr, intervals):
    """
    :param arr: list
    :param intervals: list
    :return: list
    """
    answer = []
    for open, close in intervals:
        answer += arr[open:close+1]
    return answer

print(solution([1, 2, 3, 4, 5],
               [[1, 3], [0, 4]]
               ))  # [2, 3, 4, 1, 2, 3, 4, 5]