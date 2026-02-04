# LV2 - 할인 행사 문제의 해답
def solution(want, number, discount):
    """
    :param want: list
    :param number: list
    :param discount: list
    :return: int
    """
    answer = 0
    for i in range(len(discount) - 9):
        for j in range(len(want)):
            if discount[i:i+10].count(want[j]) != number[j]:
                break
        else:
            answer += 1
    return answer

want = ["banana", "apple", "rice", "pork", "pot"]
number = [3, 2, 2, 2, 1]
discount = ["chicken", "apple", "apple", "banana", "rice", 
            "apple", "pork", "banana", "pork", "rice", "pot", 
            "banana", "apple", "banana"]
print(solution(want, number, discount))  # 3

want = ["apple"]
number = [10]
discount = ["banana", "banana", "banana", "banana", "banana", 
            "banana", "banana", "banana", "banana", "banana"]
print(solution(want, number, discount))  # 0