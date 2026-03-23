# LV2 - 뒤에 있는 큰 수 찾기 문제의 해답
def solution(numbers):
    """
    Before:
        - 단순하게 이중 for문을 사용해서 O(n^2) 시간 복잡도로 계산
    After:
        - Stack을 적용해서 O(n) 시간 복잡도로 계산
    :param numbers: list
    :return: list
    """
    answer = [-1] * len(numbers)
    stack = []
    
    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            idx = stack.pop()
            answer[idx] = numbers[i]
        stack.append(i)
        
    return answer

print(solution([2, 3, 3, 5]))  # [3, 5, 5, -1]
print(solution([9, 1, 5, 3, 6, 2]))  # [-1, 5, 6, 6, -1, -1]