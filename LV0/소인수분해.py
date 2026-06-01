# LV0 - 소인수분해 문제의 해답
def solution(n: int) -> list:
    """주어진 정수(n)을 소인수분해하는 값들을 찾습니다.

    Args:
        n (int): 주어진 정수.

    Returns:
        list[int]: 모든 소인수분해 값으로 구성된 정수 리스트.    
    """
    answer = []
    term = 2
    while True:
        if n == 1:
            break
            
        if n % term == 0:
            answer.append(term)
            n //= term
        else:
            term += 1
    return sorted(list(set(answer)))

print(solution(12))   # [2, 3]
print(solution(17))   # [17]
print(solution(420))  # [2, 3, 5, 7]