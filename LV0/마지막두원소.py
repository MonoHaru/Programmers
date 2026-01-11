# LV0 - 마지막 두 원소 문제의 해답
def solution(num_list):
    num1 = num_list[-1]
    num2 = num_list[-2]
    if num1 <= num2:
        num_list.append(num1 * 2)
    else:
        num_list.append(num1 - num2)
    return num_list