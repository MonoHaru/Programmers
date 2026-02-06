# LV0 - 문자 개수 세기
def solution(my_string):
    """
    :param my_string: str
    :return: list
    """
    dict_ = {}
    for i in range(ord('A'), ord('Z')+1):
        dict_[chr(i)] = 0
    for i in range(ord('a'), ord('z')+1):
        dict_[chr(i)] = 0
    for s in my_string:
        dict_[s] += 1
    return list(dict_.values())

print(solution("Programmers"))  
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
# 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 
# 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 
# 0, 0, 0, 0, 0, 2, 0, 1, 0, 0, 3, 
# 1, 0, 0, 0, 0, 0, 0, 0]
