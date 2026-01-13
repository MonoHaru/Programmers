# LV0 - 수열과 구간 쿼리 4 문제의 해답
def solution(arr, queries):
    for s, e, k in queries:
        for i in range(s, e+1):
            if not i % k:
                arr[i] += 1
    return arr
