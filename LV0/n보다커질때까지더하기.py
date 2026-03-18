# LV0 - n보다 커질 때까지 더하기 문제의 해답
def solution(numbers, n):
    """
    :param numbers: list
    :param n: int
    """
    answer = 0
    for num in numbers:
        answer += num
        if answer > n:
            return answer
        
print(solution([34, 5, 71, 29, 100, 34], 123))  # 139
print(solution([58, 44, 27, 10, 100], 139))  # 239