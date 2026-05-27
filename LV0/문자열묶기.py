# LV0 - 문자열 묶기 문제의 해답
def solution(strArr: list) -> int:
    """리스트에서 가장 많은 빈도의 문자열 길이를 반환합니다.

    Args:
        strArr (list[str]): 주어진 문자열 리스트.

    Returns:
        int: 최다 빈도수 문자열 길이.    
    """
    count = [0] * 31
    for word in strArr:
        count[len(word)] += 1
    return max(count)

print(solution(["a","bc","d","efg","hi"]))  # 2