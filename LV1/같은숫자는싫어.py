# LV1 - 같은 숫자는 싫어 문제의 해답
def solution(arr):
    """
    :param arr: list
    :return: list
    """
    answer = []
    for a in arr:
        if answer[-1:] == [a]:
            continue
        answer.append(a)
    return answer

print(solution([1, 1, 3, 3, 0, 1, 1]))  # [1, 3, 0, 1]
print(solution([4, 4, 4, 3, 3]))  # [4, 3]