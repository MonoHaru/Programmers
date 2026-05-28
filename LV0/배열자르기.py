# LV0 - 배열 자르기 문제의 해답
def solution(numbers: list, num1: int, num2: int) -> list:
    """주어진 배열(numbers)를 num1부터 num2까지 자릅니다.

    Args:
        numbers (list[int]): 주어진 정수 배열.
        num1 (int): 시작 인덱스.
        num2 (int): 끝 인덱스.

    Returns:
        list: 잘려진 정수 배열.    
    """
    return numbers[num1 : num2 + 1]

print(solution([1, 2, 3, 4, 5], 1, 3))  # [2, 3, 4]
print(solution([1, 3, 5], 1, 2))        # [3, 5]