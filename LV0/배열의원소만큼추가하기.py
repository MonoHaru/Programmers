# LV0 - 배열의 원소만큼 추가하기 문제의 해답
def solution(arr: list) -> list:
    """
    arr 안에 원소가 원소 수만큼 추가된 리스트를 반환합니다.

    Args:
        arr (list): 입력 리스트.

    Returns:
        list: 출력 리스트
    """
    answer = []
    for a in arr:
        answer += [a] * a
    return answer

print(solution([5, 1, 4]))  # [5, 5, 5, 5, 5, 1, 4, 4, 4, 4]
print(solution([6, 6]))  # [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
print(solution([1]))  # [1]