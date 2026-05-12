# LV0 - 배열의 길이에 따라 다른 연산하기 문제의 해답
def solution(
    arr: list, 
    n: int
) -> list:
    start_num = 0 if len(arr) % 2 else 1
    for i in range(start_num, len(arr), 2):
        arr[i] += n
    return arr