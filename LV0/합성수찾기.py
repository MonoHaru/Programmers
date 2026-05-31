# LV0 - 합성수 찾기 문제의 해답
def solution(n: int) -> int:
    """주어진 자연수(n) 이하의 합성수 개수를 찾습니다.

    Args:
        n (int): 주어진 자연수.

    Returns:
        int: 합성수의 개수
    """
    answer = 0
    for i in range(4, n + 1):
        if i % 2 == 0:
            answer += 1
            continue
        
        for j in range(3, int(i ** 0.5) + 1):
            if i % j == 0:
                answer += 1
                break
                
    return answer

print(solution(10))  # 5
print(solution(15))  # 8