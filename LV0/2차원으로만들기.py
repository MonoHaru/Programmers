# LV0 - 2차원으로 만들기 문제의 해답
def solution(num_list: list, n: int) -> list:
    """주어진 배열(num_list)를 n개씩 나눠 2차원 배열로 만듭니다.

    Args:
        num_list (list[int]): 주어진 배열.
        n (int): 나누어질 개수
        
    Returns:
        list[int]: 만들어진 2차원 배열.    
    """
    answer = []
    for i in range(len(num_list) // n):
        answer.append(num_list[i * n : (i + 1) * n])
    return answer

print(solution([1, 2, 3, 4, 5, 6, 7, 8]	, 2))  # [[1, 2], [3, 4], [5, 6], [7, 8]]