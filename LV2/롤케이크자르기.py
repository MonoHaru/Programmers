# LV2 - 롤케이크 자르기 문제의 해답
def solution(topping):
    """
    :param topping: list
    :return: int
    """
    from collections import Counter
    answer = 0
    dic = Counter(topping)
    set_dic = set()
    
    for i in topping:
        dic[i] -= 1
        set_dic.add(i)
        if dic[i] == 0:
            dic.pop(i)
        if len(dic) == len(set_dic):
            answer += 1
            
    return answer

print(solution([1, 2, 1, 3, 1, 4, 1, 2]))  # 2
print(solution([1, 2, 3, 1, 4]))  # 0