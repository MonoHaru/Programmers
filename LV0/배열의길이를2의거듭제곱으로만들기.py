# LV0 - 배ㅕㄹ의 길이를 2의 거듭제곱으로 만들기 문제의 해답
def solution(arr: list[int]) -> list[int]:
    """입력 배열의 길이를 2의 제곱으로 만듭니다.

    배열의 길이가 2의 제곱이 되도록 [0]을 추가합니다.

    Args:
        arr (list[int]): 정수가 포함한 입력 배열.

    Returns:
        list[int]: 길이가 2의 거듭제곱으로 조정된 배열.
                   기존 배열의 뒤에 부족한 만큼 0을 추가합니다.    
    """
    import math
    
    x = math.log2(len(arr))
    if int(x) == x:
        return arr
    
    return arr + [0] * (2 ** (int(x) + 1) - len(arr))

print(solution([1, 2, 3, 4, 5, 6]))  # [1, 2, 3, 4, 5, 6, 0, 0]
print(solution([58, 172, 746, 89]))  # [58, 172, 746, 89]