# LV0 - 빈 배열에 추가, 삭제하기 문제의 해답
def solution(
    arr: list, 
    flag: list
) -> list:
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