# LV0 - 조건에 맞게 수열 변환하기 1 문제의 해답
def solution(arr):
    """
    :param arr: list
    :return: list
    """
    answer = []
    for a in arr:
        if a >= 50 and a % 2 == 0:
            answer.append(a / 2)
        elif a < 50 and a % 2 == 1:
            answer.append(a * 2)
        else:
            answer.append(a)
    return answer

print(solution([1, 2, 3, 100, 99, 98]))  # [2, 2, 6, 50, 99, 49]