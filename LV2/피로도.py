# LV2 - 피로도 문제의 해답
def solution(k, dungeons):
    from itertools import permutations
    cnt = 0
    for choice in permutations(dungeons):
        cnt = max(cnt, get_count(choice, k))
    return cnt

def get_count(choice, k):
    cnt = 0
    for need, use in choice:
        if k >= need:
            k -= use
            cnt += 1
    return cnt

print(solution(80, [[80,20],[50,40],[30,10]]))