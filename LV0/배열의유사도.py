# LV0 - 배열의 유사도 문제의 해답
def solution(s1: list, s2: list) -> int:
    """같은 문자열의 갯수를 구합니다.

    Args:
        s1 (list): 주어진 문자열 리스트 1.
        s2 (list): 주어진 문자열 리스트 2.

    Returns:
        int: 겹치는 문자열 개수.    
    """
    answer = 0
    for i in range(len(s1)):
        if s1[i] in s2:
            answer += 1
    return answer

print(solution(["a", "b", "c"], ["com", "b", "d", "p", "c"]))  # 2
print(solution(["n", "omg"], ["m", "dot"]))	                   # 0