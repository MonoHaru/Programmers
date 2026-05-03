# LV0 - 배열의 원소만큼 추가하기 문제의 해답
def solution(arr: list) -> list:
    """
    리스트 arr의 각 원소가 해당 값만큼 반복하여 추가한 리스트를 반환합니다.

    Args:
        arr (list[int]): 입력 정수 리스트.

    Returns:
        list[int]: 각 원소가 값만큼 반복된 출력 리스트.
    """
    answer = []
    for a in arr:
        answer += [a] * a
    return answer

print(solution([5, 1, 4]))  # [5, 5, 5, 5, 5, 1, 4, 4, 4, 4]
print(solution([6, 6]))  # [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
print(solution([1]))  # [1]