# LV0 - 빈 배열 만들기 6 문제의 해답
def solution(arr: list[int]) -> list[int]:
    """입력 배열을 순회하며 조건에 따라 스택(stk)을 구축하여 반환합니다.

    스택의 마지막 원소가 현재 원소와 동일하면 제거(pop)하고, 
    그렇지 않으면 추가(append)하는 방식으로 배열을 재구성합니다.

    Args:
        arr (list[int]): 스택 생성의 기준이 되는 정수 배열.

    Returns:
        list[int]: 최종적으로 구성된 스택 리스트. 
                   단, 완성된 배열이 빈 배열일 경우 [-1]을 반환합니다.
    """
    stk = []
    for x in arr:
        if stk and stk[-1] == x:
            stk.pop()
        else:
            stk.append(x)
            
    return stk or [-1]

print(solution([0, 1, 1, 1, 0]))  # [0, 1, 0]
print(solution([0, 1, 0, 1, 0]))  # [0, 1, 0, 1, 0]
print(solution([0, 1, 1, 0]))  # [-1]