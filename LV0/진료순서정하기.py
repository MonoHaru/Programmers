# LV0 - 진료순서 정하기 문제의 해답
def solution(emergency: list) -> list:
    """응급도(emergency)를 보고 응급 순서를 정합니다.

    Args:
        emergency (list[int]): 응급도 정수 배열.

    Returns:
        list: 응급 순서 배열.    
    """
    answer = []
    emerg_sort = sorted(emergency, reverse=True)
    for e in emergency:
        answer.append(emerg_sort.index(e) + 1)
    return answer

print(solution([3, 76, 24]))            # [3, 1, 2]
print(solution([1, 2, 3, 4, 5, 6, 7]))  # [7, 6, 5, 4, 3, 2, 1]
print(solution([30, 10, 23, 6, 100]))   # [2, 4, 3, 5, 1]