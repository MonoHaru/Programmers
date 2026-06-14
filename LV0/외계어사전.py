# LV0 - 외계어 사전 문제의 해답
def solution(spell: list, dic: list) -> int:
    """주어진 스펠 spell를 모두 사용한 문자열을 dic에서 찾습니다.

    Args:
        spell (list[str]): 주어진 스펠.
        dic (list[str]): 주어진 문자열.
    
    Returns:
        int: 가능하면 1, 아니면 2를 반환합니다.    
    """
    flag = False
    for d in dic:
        for i, s in enumerate(spell):
            if s not in d:
                flag = False
                break
            else:
                flag = True
        if flag == True:
            return 1
    return 2

print(solution(["p", "o", "s"],
               ["sod", "eocd", "qixm", "adio", "soo"]))   # 2
print(solution(["z", "d", "x"],
               ["def", "dww", "dzx", "loveaw"]))          # 1
print(solution(["s", "o", "m", "d"],
               ["moos", "dzx", "smm", "sunmmo", "som"]))  #2