# LV1 - 제일 작은 수 제거하기
def solution(arr):
    """
    :param arr: list -> 정수 배열
    """
    arr.remove(min(arr))
    if arr:
        return arr
    else:
        return [-1]
    
print(solution([4, 3, 2, 1]))  # [4,3,2]
print(solution([10]))  # [-1]