# LV0 - 배열의 원소 삭제하기 문제의 해답
def solution(arr: list, delete_list: list) -> list:
    """배열 arr에서 delete_list에 있는 값 모두 삭제합니다.

    Args:
        arr (list): 삭제될 원소가 있는 배열.
        delete_list (list): 삭제할 원소가 있는 배열.

    Returns:
        list: arr에서 delete_list에 있는 값이 모두 삭제된 배열.    
    """
    for d in delete_list:
        if d in arr:
            arr.remove(d)
    return arr

print(solution([293, 1000, 395, 678, 94],
               [94, 777, 104, 1000, 1, 12]))  # [293, 395, 678]
print(solution([110, 66, 439, 785, 1],
               [377, 823, 119, 43]))  # [110, 66, 439, 785, 1]