# LV0 - 배열 만들기 5 문제의 해답
def solution(intStrs, k, s, l):
    """
    :param intStrs: list
    :param k: int
    :param s: int
    :param l: int
    :return: list
    """
    answer = []
    for intStr in intStrs:
        substr = int(intStr[s:s+l])
        if substr > k:
            answer.append(substr)
    return answer

intStrs = [
    "0123456789", 
    "9876543210",
    "9999999999999"
    ]
k = 50000
s = 5
l = 5
print(solution(intStrs, k, s, l))  # [56789, 99999]