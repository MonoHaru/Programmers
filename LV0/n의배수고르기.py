# LV0 - n의 배수 고르기 문제의 해답
def solution(n: int, numlist: list) -> list:
    """주어진 정수 리스트 numlist 원소 중 n의 배수를 찾습니다.

    Args:
        n (int): 주어진 정수.
        numlist (list[int]): 주어진 정수 리스트.

    Returns:
        list[int]: n의 배수가 모인 정수 리스트.    
    """
    answer = []
    for m in numlist:
        if not m % n:
            answer.append(m)
    return answer

print(solution(3, [4, 5, 6, 7, 8, 9, 10, 11, 12]))  # [6, 9, 12]
print(solution(5, [1, 9, 3, 10, 13, 5]))	        # [10, 5]
print(solution(12, [2, 100, 120, 600, 12, 12]))     # [120, 600, 12, 12]