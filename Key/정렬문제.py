# LV1 - 문자열 내 마음대로 정렬하기 문제의 해답
def solution(strings, n):
    """
    Before:
        - 두 번째 정렬 후, 전체 정렬 방법을 문자 위치별로 수행
    After:
        - Lamdba를 활용해 두 번째 문제를 우선적으로 정렬하고, 나머지를 전체 정렬
        - 그러면 두 번째 정렬 조건을 충족한 상태로 전체 정렬
    :param strings: list
    :param n: int
    :return: list
    """
    return sorted(strings, key=lambda x: (x[n], x))

print(solution(["sun", "bed", "car"], 1))  # ["car", "bed", "sun"]
print(solution(["abce", "abcd", "cdx"], 2))  # ["abcd", "abce", "cdx"]