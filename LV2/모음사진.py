# LV2 - 모음사전 문제의 해답
def solution(word):
    """
    :param word: str
    :return: int
    """
    from itertools import product
    vowels = ["A", "E", "I", "O", "U"]
    answer = []
    for i in range(1, 5+1):
        for j in product(vowels, repeat=i):
            answer.append("".join(j))
    answer.sort()
    return answer.index(word) + 1

print(solution("AAAAE"))  # 6
print(solution("AAAE"))  # 10
print(solution("I"))  # 1563
print(solution("EIO"))  # 1189