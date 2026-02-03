# LV2 - N개의 최소공배수 문제의 해답
def solution(arr):
    """
    :param arr: list
    :return: int
    """
    temp = max(arr)
    check = 0
    while True:
        for a in arr:
            if temp % a != 0:
                check = 1
                continue
        if check == 1:
            temp += 1
            check = 0
        else:
            return temp
        
print(solution([2, 6, 8, 14]))  # 168
print(solution([1, 2, 3]))  # 6