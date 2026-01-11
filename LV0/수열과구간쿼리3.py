# LV0 - 수열과 구간 쿼리 3 문제의 해답
def solution(arr, queries):
    for num1, num2 in queries:
        arr[num1], arr[num2] = arr[num2], arr[num1]
    return arr