# LV0 - A 강조하기 문제의 해답
def solution(myString):
    """
    :param myString: str
    :return: str
    """
    return myString.lower().replace('a', 'A')

print(solution("abstract algebra"))  # "AbstrAct AlgebrA"
print(solution("PrOgRaMmErS"))  # "progrAmmers"