# LV0 - 최댓값 만들기 (1) 문제의 해답
def solution(numbers: list) -> int:
    """주어진 정수 배열 중 가장 큰 두 원소의 곱을 구합니다.

    Args:
        numbers (list[int]): 주어진 자연수 배열.

    Returns:
        int: 가장 큰 두 원소의 곱.
    """
    numbers.sort()
    return numbers[-1] * numbers[-2]

print(solution([1, 2, 3, 4, 5]))        # 20
print(solution([0, 31, 24, 10, 1, 9]))  # 744