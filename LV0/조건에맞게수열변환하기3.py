# LV0 - 조건에 맞게 수열 변화하기 3 문제의 해답
def solution(arr: list, k: int) -> list:
    """조건에 맞게 새로운 리스트를 만듭니다.

    k가 홀수면 각 원소에 k만큼 곱한 값을 추가하고,

    k가 짝수면 각 원소에 k만큼 더한 값을 추가합니다.

    Args:
        arr (list[int]): 정수 리스트.
        k (int): 조건 정수.
    
    Returns:
        list: 조건에 맞게 새로 생성된 배열.    
    """
    answer = []
    for a in arr:
        if k % 2 == 1:
            answer.append(a * k)
        else:
            answer.append(a + k)
    return answer