# LV1 - 문자열 내 마음대로 정렬하기 문제의 해답
def solution(strings, n):
    """
    두 번째 문자로 정렬 후, 전체로 정렬
    :param strings: list
    :param n: int
    :return: list
    """
    return sorted(strings, key=lambda x: (x[n], x))

print(solution(["sun", "bed", "car"], 1))  # ["car", "bed", "sun"]
print(solution(["abce", "abcd", "cdx"], 2))  # ["abcd", "abce", "cdx"]