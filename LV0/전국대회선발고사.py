# LV0 - 전국 대회 선발 고사 문제의 해답
def solution(
    rank: list, 
    attendance: list
) -> int:
    """
    Args:
        rank (list): ...
        attendance (list): ...
    Returns:
        int: ...
    """
    answer = {}
    for i, (value, flag) in enumerate(zip(rank, attendance)):
        if flag:
            answer[i] = value
    a, b, c = sorted(answer.items(), key=lambda x: x[1])[:3]
    return 10000 * a[0] + 100 * b[0] + c[0]

print(solution([3, 7, 2, 5, 4, 6, 1],
               [false, true, true, true, true, false, false]))  # 20403
print(solution([1, 2, 3], 
               [true, true, true]))  # 102
print(solution([6, 1, 5, 2, 3, 4],
               [true, false, true, false, false, true]))  # 50200