# LV0 - 빈 배열에 추가, 삭제하기 문제의 해답
def solution(
    arr: list[int], 
    flag: list[bool]
) -> list[int]:
    """flag 값에 따라 배열을 동적으로 구성하여 반환합니다.

    각 원소의 flag 값이 True인 경우 해당 원소를 (원소 값 * 2)번 추가하고,
    False인 경우 배열의 끝에서 해당 원소 값만큼 요소를 제거합니다.
    
    Args:
        arr (list[int]): 처리에 사용할 양의 정수 리스트.
        flag (list[bool]): 각 원소에 대한 작업 종류(추가/삭제)를 결정하는 불리언 리스트.

    Returns:
        list[int]: 조건에 따라 최종적으로 구성된 정수 리스트.
    """
    answer = []
    for i, j in zip(arr, flag):
        if j:
            answer.extend([i] * (i * 2))
        else:
            answer = answer[:-i]
    return answer

print(solution(
    [3, 2, 4, 1, 3], 
    [true, false, true, false, false]
)) # [3, 3, 3, 3, 4, 4, 4, 4]