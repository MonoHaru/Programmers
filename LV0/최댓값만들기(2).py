# LV0 - 최댓값 만들기 (2) 문제의 해답
def solution(numbers: list) -> int:
    """두 수의 곱이 가장 큰 값을 구하시오.

    Args:
        numbers (list[int]): 주어진 정수 리스트.

    Returns:
        int: 최대 곱.    
    """
    numbers.sort()
    return max(numbers[-1] * numbers[-2], numbers[0] * numbers[1])

print(solution([1, 2, -3, 4, -5]))          # 15
print(solution([0, -31, 24, 10, 1, 9]))     # 240
print(solution([10, 20, 30, 5, 5, 20, 5]))  # 600