# LV1 - 카드 뭉치 문제의 해답
def solution(cards1, cards2, goal):
    """
    :param cards1: list
    :param cards2: list
    :return: list
    """
    for g in goal:
        if cards1 and g == cards1[0]:
            cards1.pop(0)
        elif cards2 and g == cards2[0]:
            cards2.pop(0)
        else:
            return "No"
    return "Yes"

print(solution(["i", "drink", "water"], 
               ["want", "to"], 
               ["i", "want", "to", "drink", "water"]))  # Yes
print(solution(["i", "water", "drink"], 
               ["want", "to"],
               ["i", "want", "to", "drink", "water"]))  # "No"