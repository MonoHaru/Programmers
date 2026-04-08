# LV0 - 1로 만들기 문제의 해답
def solution(num_list):
    """
    :param num_list: list
    :return: int
    """
    answer = 0
    for i in range(len(num_list)):
        temp = num_list[i]
        while temp != 1:
            answer += 1
            
            if temp % 2 == 0:
                temp //= 2
            else:
                temp = (temp - 1) // 2
                
    return answer

print(solution([12, 4, 15, 1, 14]))  # 11