# LV0 - 수열과 구간 쿼리 2 문제의 해답
def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        tmp = []
        for x in sorted(arr[s:e+1]):
            if x > k:
                tmp.append(x)
                break
        answer.append(-1 if not tmp else tmp[0])
    return answer