# LV0 - 순서쌍의 개수 문제의 해답
def solution(n: int) -> int:
    """두 자연수의 곱이 n이 되는 쌍의 개수를 구합니다.

    Args:
        n (int): 두 수의 곱이 되는 수.

    Returns:
        int: 곱의 쌍의 개수.    
    """
    answer = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            answer += 2
            
            if i * i == n:
                answer -= 1
    return answer

print(solution(20))   # 6
print(solution(100))  # 9