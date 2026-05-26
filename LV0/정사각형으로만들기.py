# LV0 - 정사각형으로 만들기 문제의 해답
def solution(arr: list) -> list:
    """직사각형 모양의 arr에 0을 추가해 정사각형 모양으로 만듭니다.

    Args:
        arr (list[int]): 직사각형 모양의 이차원 정수 배열.

    Returns:
        list: 정사각형 모양의 이차원 정수 배열.    
    """
    len_raw, len_col = len(arr), len(arr[0])
    if len_raw < len_col:
        for i in range(len_col - len_raw):
            arr.append([0] * (len_col))
    elif len_raw > len_col:
        for i in range(len_raw):
            arr[i].extend([0] * (len_raw - len_col))
    return arr

print(solution([[572, 22, 37], 
                [287, 726, 384], 
                [85, 137, 292], 
                [487, 13, 876]]))
""""
[[572, 22, 37, 0], 
[287, 726, 384, 0], 
[85, 137, 292, 0], 
[487, 13, 876, 0]]
"""
print(solution([[57, 192, 534, 2], 
                [9, 345, 192, 999]]))
"""
[[57, 192, 534, 2], 
[9, 345, 192, 999], 
[0, 0, 0, 0], 
[0, 0, 0, 0]]
"""
print(solution([[1, 2], [3, 4]]	))
"""
[[1, 2], 
[3, 4]]
"""