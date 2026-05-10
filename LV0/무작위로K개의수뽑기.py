# LV0 - 무작위로 K개의 수 뽑기 문제의 해답
def solution(
    arr: list[int], 
    k: int
) -> list[int]:
    """입력 배열에서 중복을 제거하여 순서를 유지한 채 K개의 원소를 추출합니다.

    배열의 원소를 순차적으로 확인하며, 이전에 등장하지 않은 원소만 선택합니다.
    최종 결과 배열의 길이가 k보다 작으면 나머지 공간을 -1로 채웁니다.

    Args:
        arr (list[int]): 중복된 정수를 포함할 수 있는 원본 배열.
        k (int): 결과로 반환할 배열의 목표 길이.

    Returns:
        list[int]: 중복이 제거된 원소들로 구성된 길이 k의 리스트.
                   길이가 부족할 경우 뒤에 -1이 채워진 상태로 반환됩니다.
    """
    arr = list(dict.fromkeys(arr))
    if len(arr) >= k:
        return arr[:k]
    else:
        arr.extend([-1] * (k - len(arr)))
        return arr
    
print(solution([0, 1, 1, 2, 2, 3], 3))  # [0, 1, 2]
print(solution([0, 1, 1, 1, 1], 4))  # [0, 1, -1, -1]