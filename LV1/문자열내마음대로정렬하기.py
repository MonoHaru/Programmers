# LV1 - 문자열 내 마음대로 정렬하기
def solution(strings, n):
    """
    :param strings: list
    :param n: int
    :return: list
    """
    return sorted(strings, key=lambda x: (x[n], x))

print(solution(["sun", "bed", "car"], 1))  # ["car", "bed", "sun"]
print(solution(["abce", "abcd", "cdx"], 2))  # ["abcd", "abce", "cdx"]