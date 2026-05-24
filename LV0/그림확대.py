# LV0 - 그림 확대 문제의 해답
def solution(picture: list, k: int) -> list:
    """그림 리스트 picture를 k배로 늘립니다.

    Args:
        picture (list[str]): 그림 리스트.

    Returns:
        k: 배수.    
    """
    answer = []
    for raw in picture:
        sub = ''
        for x in raw:
            if x == 'x':
                sub += 'x'* k
            else:
                sub += '.' * k
        for _ in range(k):
            answer.append(sub)
    return answer

print(solution([
    ".xx...xx.", 
    "x..x.x..x", 
    "x...x...x", 
    ".x.....x.", 
    "..x...x..", 
    "...x.x...", 
    "....x...."
], 2))
"""
[
"..xxxx......xxxx..", 
"..xxxx......xxxx..", 
"xx....xx..xx....xx", 
"xx....xx..xx....xx", 
"xx......xx......xx", 
"xx......xx......xx", 
"..xx..........xx..", 
"..xx..........xx..", 
"....xx......xx....", 
"....xx......xx....", 
"......xx..xx......", 
"......xx..xx......", 
"........xx........", 
"........xx........"
]
"""
print(solution(["x.x", ".x.", "x.x"], 3))
"""
[
"xxx...xxx", 
"xxx...xxx", 
"xxx...xxx", 
"...xxx...", 
"...xxx...", 
"...xxx...", 
"xxx...xxx", 
"xxx...xxx", 
"xxx...xxx"
]
"""
