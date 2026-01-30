# LV0 - 접미사 배열 문제의 해답
def solution(my_string):
    """
    :param my_string: str
    :return: str
    """
    return sorted([my_string[i:] for i in range(len(my_string))])

print(solution("banana"))  
# ["a", "ana", "anana", "banana", "na", "nana"]

print(solution("programmers"))  
# ["ammers", "ers", "grammers", "mers", "mmers", "ogrammers", 
# "programmers", "rammers", "rogrammers", "rs", "s"]
