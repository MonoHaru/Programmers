# LV0 - 원소들의 곱과 합 문제의 해답
from math import prod

def solution(num_list):
    return int(prod(num_list) < sum(num_list)**2) 