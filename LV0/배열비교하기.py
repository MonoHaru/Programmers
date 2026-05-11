# LV0 - 배열 비교하기 문제의 해답
def solution(
    arr1: list[int], 
    arr2: list[int],
) -> int:
    """두 정수 배열의 대소관계를 파악하여 정수를 반환합니다.

    두 배열의 길이가 다르면, 배열의 길이가 긴 쪽이 더 큽니다.
    길이가 같다면, 원소의 총합을 비교해 더 큰 쪽이 큽니다.

    Args:
        arr1 (list[int]): 비교할 첫 번째 정수 배열.
        arr2 (list[int]): 비교할 두 번째 정수 배열.

    Returns:
        int: 비교 결과에 따른 정수값.
    """
    if len(arr1) == len(arr2):
        if sum(arr1) > sum(arr2):
            return 1
        elif sum(arr1) < sum(arr2):
            return -1
        else:
            return 0
    elif len(arr1) > len(arr2):
        return 1
    else:
        return -1
    
print(solution([49, 13], [70, 11, 2]))  # -1
print(solution([100, 17, 84, 1], [55, 12, 65, 36]))  # 1
print(solution([1, 2, 3, 4, 5], [3, 3, 3, 3, 3]))  # 0