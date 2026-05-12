# LV0 - 문자열 묶기 문제의 해답
def solution(strArr: list[str]) -> int:
    answer = dict()
    for s in strArr:
        answer[len(s)] = answer.get(len(s), 0) + 1
    return max(answer.values())

print(solution(["a","bc","d","efg","hi"]))  # 2