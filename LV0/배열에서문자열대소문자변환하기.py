# LV0 - 배열에서 문자열 대소문자 변환하기 문제의 해답
def solution(strArr):
    """
    :param strArr: list
    :return: list
    """
    return [s.upper() if i % 2 else s.lower() for i, s in enumerate(strArr)]

print(solution(["AAA","BBB","CCC","DDD"]))  # ["aaa","BBB","ccc","DDD"]
print(solution(["aBc","AbC"]))  # ["abc","ABC"]